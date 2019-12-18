from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from users.models import User
from django.contrib.auth.models import Group


class UserAdmin(BaseUserAdmin):
    search_fields = ['username', 'email', 'first_name', 'last_name']
    list_display = ('username', 'first_name', 'last_name', 'role', 'is_active', 'is_superuser',)
    fieldsets = (
        ('Login', {'fields': (
            'username',
            'password'
        )}),
        ('Personal Information', {'fields': (
            'first_name',
            'last_name',
            'email',
        )}),
        ('University', {'fields': (
            'role',
        )}),
        ('Permissions', {'fields': (
            'is_active',
            'is_superuser',
        )}),
    )


# Register User model
admin.site.register(User, UserAdmin)

# Unregister Django's builtin user group model
admin.site.unregister(Group)
