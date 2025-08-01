from django.urls import path
from . import views

urlpatterns =[
    path('create/', views.create_book, name='create_book'),
    path('edit/<int:pk>/', views.edit_book, name='edit_book'),
    path('view/', views.book_list, name='book_list')

]