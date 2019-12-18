from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ADMIN = 1
    UNIVERSITY_ADMIN = 2
    FACULTY = 3
    STUDENT = 4
    ROLE_CHOICES = (
        (STUDENT, 'Student'),
        (FACULTY, 'Faculty'),
        (UNIVERSITY_ADMIN, 'University Admin'),
        (ADMIN, 'Admin'),
    )

    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    role = models.PositiveSmallIntegerField('user role', choices=ROLE_CHOICES, default=4)

    REQUIRED_FIELDS = ['email']

    def is_admin(self):
        return self.role == self.ADMIN

    def is_university_admin(self):
        return self.role == self.UNIVERSITY_ADMIN

    def is_faculty(self):
        return self.role == self.FACULTY

    def is_student(self):
        return self.role == self.STUDENT

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
