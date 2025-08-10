# LibraryProject

## Permissions and Group Creation in Bookshelf App (Django)

### Permissions Added (in models.py)
```python
# Example permission definition in models.py
class Meta:
    permissions = [
        ('can_view', 'Can view books'),
        ('can_create', 'Can create books'),
        ('can_edit', 'Can edit books'),
        ('can_delete', 'Can delete books'),
    ]
Groups (via Admin or script)

python
# Example group creation script
from django.contrib.auth.models import Group, Permission

viewers, _ = Group.objects.get_or_create(name='Viewers')
editors, _ = Group.objects.get_or_create(name='Editors')
admins, _ = Group.objects.get_or_create(name='Admins')

# Assign permissions
viewers.permissions.add(Permission.objects.get(codename='can_view'))
# ... similar for other groups
Views Protected (in views.py)

python
from django.contrib.auth.decorators import permission_required

@permission_required('bookshelf.can_view')
def book_list(request):
    pass

@permission_required('bookshelf.can_create')
def add_book(request):
    pass

@permission_required('bookshelf.can_edit')
def edit_book(request):
    pass

@permission_required('bookshelf.can_delete')
def delete_book(request):
    pass
W11 Task 2: Django Security Best Practices
Security Configurations

1. CSRF Protection (Enabled by default)

html
<!-- In templates -->
<form method="post">
    {% csrf_token %}
    <!-- form fields -->
</form>
2. Content Security Policy (CSP)

python
# settings.py
INSTALLED_APPS = [
    ...
    'csp',
    ...
]

CONTENT_SECURITY_POLICY = {
    'default-src': "'self'",
    'script-src': ["'self'", 'https://cdnjs.cloudflare.com'],
    'style-src': ["'self'", 'https://fonts.googleapis.com'],
    'font-src': ["'self'", 'https://fonts.gstatic.com'],
}
3. Clickjacking Protection

python
# settings.py
X_FRAME_OPTIONS = 'DENY'
4. Secure Cookies

python
# settings.py
SESSION_COOKIE_HTTPONLY = True
CSRF_COOKIE_HTTPONLY = True
SESSION_COOKIE_SECURE = True  # Requires HTTPS
CSRF_COOKIE_SECURE = True     # Requires HTTPS
5. HSTS Settings

python
# settings.py
SECURE_HSTS_SECONDS = 31536000  # 1 year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
6. Other Security Headers

python
# settings.py
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
W11 Task 3: HTTPS Enforcement
HTTPS Configuration

python
# settings.py
SECURE_SSL_REDIRECT = True  # Redirect all HTTP to HTTPS
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')  # For proxy setups
Production Deployment

bash
# Example Nginx configuration for HTTPS
server {
    listen 443 ssl;
    server_name example.com;
    
    ssl_certificate /path/to/cert.pem;
    ssl_certificate_key /path/to/key.pem;
    
    location / {
        proxy_pass http://localhost:8000;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
🚀 Setup Instructions

1. Clone and Setup Environment

bash
git clone https://github.com/yourusername/LibraryProject.git
cd LibraryProject
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows
pip install -r requirements.txt
2. Database Setup

bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
3. Run Development Server

bash
python manage.py runserver
4. Production Deployment

bash
# Using Gunicorn + Nginx
gunicorn --bind 0.0.0.0:8000 LibraryProject.wsgi
📝 Notes

Replace placeholder values with your actual configuration
For production, always use HTTPS and proper secret key management
Regularly update dependencies for security patches