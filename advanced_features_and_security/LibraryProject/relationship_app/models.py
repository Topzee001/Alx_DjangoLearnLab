from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser, BaseUserManager



# Create your models here.

class Author(models.Model):
    name =models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    class Meta:
        permissions = [
            ("can_add_book", "Can add book"),
            ("can_change_book", "Can change book"),
            ("can_delete_book", "Can delete book"),
                            ]

    def __str__(self):
        return self.title


class Library(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book, related_name='libraries')

    def __str__(self):
        return self.name



class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    ROLES_CHOICES =(
        ('Admin', 'Admin'),
        ('Librarian', 'Librarian'),
        ('Member', 'Member'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role= models.CharField(max_length=20, choices=ROLES_CHOICES, default='Member')

    def __str__(self):
        return f"{self.user.username} - {self.role}"
    

# CREATING CUSTOM USERS

class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, date_of_birth, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, date_of_birth=date_of_birth, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, date_of_birth, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True')

        return self.create_user(username, email, date_of_birth, password, **extra_fields)



class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_picture/', null=True, blank=True)

    objects = CustomUserManager()


    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['date_of_birth']




    def __str__(self):
        return self.username
        
