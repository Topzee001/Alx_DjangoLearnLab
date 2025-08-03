from django.urls import path, include
from .views import BookList
from rest_framework import routers
from .views import BookViewSet

# Create your views here.
router = routers.DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')


urlpatterns = [
    path('', include(router.urls)),
    path('books/', BookList.as_view(), name='book-list'),
]