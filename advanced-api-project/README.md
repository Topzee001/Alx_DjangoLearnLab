# Advanced API Project

This Django REST Framework (DRF) project implements CRUD operations for a Book model using generic views, with custom validation, permissions, and filtering.

## Setup

Install dependencies: pip install django djangorestframework django-filter.

Apply migrations: python manage.py makemigrations && python manage.py migrate.

Create a superuser: python manage.py createsuperuser.

Run the server: python manage.py runserver.

## Endpoints

GET /books/: List all books. Supports filtering by author (e.g., /books/?author=John%20Doe). Read-only for unauthenticated users.

GET /books/int:pk/: Retrieve a book by ID. Read-only for unauthenticated users.

POST /books/create/: Create a new book. Requires authentication. Expects JSON like {"title": "Book Title", "author": "Author Name", "publication_year": 2000}.

PUT/PATCH /books/update/int:pk/: Update a book by ID. Requires authentication. Supports partial updates (PATCH).

DELETE /books/int:pk/delete/: Delete a book by ID. Requires authentication.

## View Configurations

BookListView: Uses ListAPIView with DjangoFilterBackend for author filtering. Permissions: IsAuthenticatedOrReadOnly.

BookDetailView: Uses RetrieveAPIView. Permissions: IsAuthenticatedOrReadOnly.

BookCreateView: Uses CreateAPIView. Sets created_by to the authenticated user. Permissions: IsAuthenticated.

BookUpdateView: Uses UpdateAPIView. Updates created_by to the authenticated user. Permissions: IsAuthenticated.

BookDeleteView: Uses DestroyAPIView. Permissions: IsAuthenticated.

## Validation

The BookSerializer enforces:

Title must be at least 3 characters.

Publication year must not be a future year.

Validation errors return a 400 response with details, e.g., {"title": ["Title must be at least 3 characters long."]}.

## Permissions

Read operations (GET): Accessible to all users (authenticated or not).

Write operations (POST, PUT, PATCH, DELETE): Restricted to authenticated users via IsAuthenticated.

## Testing

Use Postman or curl to test endpoints:

List books: curl http://localhost:8000/books/

Create book: curl -X POST -H "Authorization: Token <your-token>" -H "Content-Type: application/json" -d '{"title": "Test Book", "author": "Test Author", "publication_year": 2020}' http://localhost:8000/books/create/

Test invalid data: Send a POST with {"title": "A", "publication_year": 1800} to verify 400 response.

Test permissions: Attempt a POST without a token to verify 401 response.

## Notes

Ensure DRF token authentication is configured (rest_framework.authtoken in INSTALLED_APPS).

The created_by field links books to the user who created/updated them, set automatically in perform_create and perform_update.

Filtering is enabled for the author field in the list view.

## Book API Test
- CRUD operations for Book API
- Filtering by title
- Searching by author name
- Ordering by publication_year
- Permission enforcement for create/update/delete

Run tests:
python manage.py test api
