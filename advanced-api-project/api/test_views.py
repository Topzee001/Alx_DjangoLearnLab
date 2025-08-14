from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Book, Author

class BookAPITestCase(APITestCase):

    def setUp(self):
        # create a user for authenticated actions
        self.user = User.objects.create_user(username='testibro', password='ib@123456')

        # create an author
        self.author = Author.objects.create(name="J.K. Rowling")

        # create some books
        self.book1 = Book.objects.create(
            title = "Harry Potter 1",
            author=self.author,
            publication_year=1999
        )

        self.book2 = Book.objects.create(
            title = "Harry Potter 2",
            author=self.author,
            publication_year=1997
        )

        # Urls patterns

        self.list_url = reverse('book-list')
        self.create_url = reverse('book-create')
        self.update_url = lambda pk: reverse('book-update', args=[pk])
        self.details_url = lambda pk: reverse('book-detail', args=[pk])
        self.delete_url = lambda pk: reverse('book-delete', args=[pk])

    # list books
    def test_list_books(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    # create book, authenticated user
    def test_create_books_authenticated(self):
        self.client.login(username='testibro', password='ib@123456')
        data= {
            'title': 'New Book',
            "author_id": self.author.id,
            'publication_year': 2022
        }
        
        response = self.client.post(self.create_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    # create book, unauthenticated
    def test_create_book_unauthenticated(self):
        data= {
            'title': 'New Book',
            "author_id": self.author.id,
            'publication_year': 2022
        }
        
        response = self.client.post(self.create_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_book(self):
        self.client.login(username='testibro', password='ib@123456')
        data ={
            'title': 'Updated book',
            "author_id": self.author.id,
            'publication_year': 1859
        }

        response = self.client.put(self.update_url(self.book1.id), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated book")

    def test_delete_book(self):
        self.client.login(username='testibro', password='ib@123456')
        response = self.client.delete(self.delete_url(self.book1.id))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    def test_filter_books_by_title(self):
        response = self.client.get(f"{self.list_url}?title=Harry Potter 1")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_search_book(self):
        response = self.client.get(f"{self.list_url}?search=Rowling")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(any("Rowling" in b['author'] for b in response.data))
        # or use this method
        # Search check
        # authors = [b['author'] for b in response.data]
        # self.assertIn("J.K. Rowling", authors)

    def test_order_books_by_publication_year(self):
        response = self.client.get(f"{self.list_url}?ordering=-publication_year")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        years = [book['publication_year'] for book in response.data]
        # self.assertEqual(years, sorted(years, reverse=True))
        self.assertTrue(all(years[i] >= years[i+1] for i in range(len(years) -1)))

    


