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
