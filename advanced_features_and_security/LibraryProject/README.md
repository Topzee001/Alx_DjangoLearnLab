# LibraryProject
# permissions and group creation in bookshelf app in django

## Permissions Added (in models.py)
- can_view
- can_create
- can_edit
- can_delete

## Groups (via Admin or script)
- **Viewers**: can_view
- **Editors**: can_view, can_create, can_edit
- **Admins**: all permissions

## Views Protected (in views.py)
- book_list: @permission_required('your_app.can_view')
- add_book: @permission_required('your_app.can_create')
- edit_book: @permission_required('your_app.can_edit')
- delete_book: @permission_required('your_app.can_delete')

This is a basic Django project created to practice the Django setup process.

# W11 Task 2
🔐 Django Security Best Practices – Task 2 (ALX Django Learn Lab)
This Django project demonstrates how to implement key security best practices to protect your application from common web vulnerabilities. These implementations help strengthen your Django app against attacks like CSRF, XSS, Clickjacking, and more.
📌 Features Implemented
✅ 1. Cross-Site Request Forgery (CSRF) Protection
CSRF protection is enabled by default in Django.
All form submissions use the {% csrf_token %} template tag to protect against forged requests.
✅ 2. Content Security Policy (CSP)
Integrated using the django-csp package.
CSP restricts where scripts, styles, and fonts can be loaded from.
# settings.py
CONTENT_SECURITY_POLICY = {
    'DIRECTIVES': {
        'default-src': ("'self'",),
        'font-src': ("'self'", 'https://fonts.gstatic.com'),
        'script-src': ("'self'", 'https://cdnjs.cloudflare.com'),
        'style-src': ("'self'", 'https://fonts.googleapis.com'),
    }
}
⚠️ The CSP configuration was updated to the latest format as required in django-csp v4.0+.
✅ 3. Clickjacking Protection
Added the X-Frame-Options header to deny embedding of pages in iframes.
# settings.py
X_FRAME_OPTIONS = 'DENY'
✅ 4. XSS Protection
Django autoescapes template content by default.
Ensured user-generated content is properly escaped.
✅ 5. Secure Cookies
Cookies are marked as HttpOnly and Secure where applicable.
# settings.py
SESSION_COOKIE_HTTPONLY = True
CSRF_COOKIE_HTTPONLY = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
✅ 6. Strict Transport Security
Enforced HTTPS using the Strict-Transport-Security header.
# settings.py
SECURE_HSTS_SECONDS = 31536000  # 1 year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
✅ 7. Other Security Headers
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
🧪 How to Run the Project
Clone the Repository
git clone <your-repo-url>
cd LibraryProject
Create Virtual Environment & Install Requirements
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
Run Migrations
python manage.py makemigrations
python manage.py migrate
Start Development Server
python manage.py runserver
