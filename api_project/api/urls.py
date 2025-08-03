from django.urls import path
from .views import BookList

# Create your views here.


urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
]