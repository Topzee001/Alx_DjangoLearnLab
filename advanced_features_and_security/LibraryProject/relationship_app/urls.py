from django.urls import path
from .views import list_books, LibraryDetailView
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', views.register_view, name='register'),
    path('admin-page/', views.admin_view, name='admin_page'),
    path('librarian-page/', views.librarian_view, name='librarian_page'),
    path('member-page/', views.member_view, name='member_page'),
    path('books/add_book/', views.add_book, name='add_book'),
    path('book/<int:pk>/edit_book/', views.edit_book, name='edit_book'),
    path('book/<int:pk>/delete/', views.delete_book, name='delete_book')

]