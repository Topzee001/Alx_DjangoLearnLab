from rest_framework import serializers
from .models import Book, Author
from django.utils import timezone

class BookSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    author_id = serializers.PrimaryKeyRelatedField(
        queryset=Author.objects.all(), write_only=True
    )
    """
    Serializes Book model fields and validates publication_year.
    """
    class Meta:
        model = Book
        fields = "__all__"

    def create(self, validated_data):
        author = validated_data.pop('author_id')
        validated_data['author'] = author
        return super().create(validated_data)

    def update(self, instance, validated_data):
        if 'author_id' in validated_data:
            author = validated_data.pop('author_id')
            validated_data['author'] = author
        return super().update(instance, validated_data)

    def validate_title(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Title must be at least 3 characters")
        return value

    def validate_publication_year(self, data):
        current_year = timezone.now().year
        if data > current_year:
            raise serializers.ValidationError("Publication year cannot be a future year")
        return data


class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializes Author model and includes nested books.
    """

    books= BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ["name", "books"]


