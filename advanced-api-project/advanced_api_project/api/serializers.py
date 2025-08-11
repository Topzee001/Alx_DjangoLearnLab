from rest_framework import serializers
from .models import Book, Author
from django.utils import timezone

class BookSerializer(serializers.ModelSerializer):
    """
    Serializes Book model fields and validates publication_year.
    """
    class Meta:
        model = Book
        fields = "__all__"

    def validate_publication_year(self, data):
        current_year = timezone.now().year
        if data < current_year:
            raise serializers.ValidationError("Publication year cannot be a future year")
        return data


class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializes Author model and includes nested books.
    """

    books= BookSerializer(many= True, read_only=True)

    class Meta:
        model = Author
        fields = ["name", "books"]


