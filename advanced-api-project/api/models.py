from django.db import models

# Create your models here.
class Author(models.Model):
    """
    Author model to store writer's information.
    """
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name
    
class Book(models.Model):
    """
    Book model to store book details.
    Linked to Author with a ForeignKey relationship.
    """
    title = models.CharField(max_length=150)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")
    created_by = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.title} {self.publication_year}"