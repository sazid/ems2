from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from core.models import (
    User,
    University,
    Course,
    Exam,
    Question,
    McqChoices,
)


admin.site.site_title = 'EMS Admin'
admin.site.site_header = 'Exam Management System'


class UserAdmin(BaseUserAdmin):
    search_fields = ['username', 'email', 'first_name', 'last_name']
    list_display = ('username', 'first_name', 'last_name',)
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
            'university',
        )}),
        ('Permissions', {'fields': (
            'is_active',
            'is_staff',
            'is_superuser',
        )}),
    )


# Register models
admin.site.register(User, UserAdmin)
admin.site.register(University)
admin.site.register(Course)
admin.site.register(Exam)
admin.site.register(Question)
admin.site.register(McqChoices)

# Unregister Django's builtin user group model
admin.site.unregister(Group)
