# Django Blog CRUD (Week 14 refresher)

Features
- Public post list + detail
- Authenticated create
- Author-only edit/delete
- Pagination (optional)

Endpoints (HTML)
- GET  /post/                 → list
- GET  /post/<pk>/            → detail
- GET  /post/new/             → create form (login required)
- POST /post/new/             → create (login required)
- GET  /post/<pk>/edit/       → edit form (author only)
- POST /post/<pk>/edit/       → update (author only)
- GET  /post/<pk>/delete/     → confirm delete (author only)
- POST /post/<pk>/delete/     → delete (author only)

Auth
- /accounts/login/ (Django auth)
- /accounts/logout/

Setup
1) pip install django
2) add `blog` to INSTALLED_APPS
3) `python manage.py migrate`
4) `python manage.py createsuperuser`
5) `python manage.py runserver`
