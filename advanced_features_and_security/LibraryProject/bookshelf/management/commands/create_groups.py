from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.apps import apps
# this code is for creating groups and assigning permissions to users using code
class Command(BaseCommand):
    help = "Create default groups and assign permissions"

    def handle(self, *args, **kwargs):
        book_model = apps.get_model("bookshelf", "Book")

        permissions = {
            "Viewers": ["can_view"],
            "Editors": ["can_view", "can_edit", "can_create"],
            "Admins": ["can_view", "can_edit", "can_create", "can_delete"]
        }

        for group_name, perms in permissions.items():
            group, created = Group.objects.get_or_create(name=group_name)
            for perm_code in perms:
                perm = Permission.objects.get(codename=perm_code, content_type__app_label="bookshelf")
                group.permissions.add(perm)
            self.stdout.write(self.style.SUCCESS(f"Group '{group_name}' updated."))
