from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.db import models


class University(models.Model):
    name = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


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
    university = models.ForeignKey(University, on_delete=models.DO_NOTHING, blank=True, null=True)

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


class Course(models.Model):
    name = models.CharField(max_length=500)
    code = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)

    university = models.ForeignKey(University, on_delete=models.CASCADE)

    def __str__(self):
        return f'[{self.code}] {self.name}'


class Exam(models.Model):
    name = models.CharField(max_length=500)
    start = models.DateTimeField()
    end = models.DateTimeField()

    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} {self.course}'


class Question(models.Model):
    QUESTION_TYPE_MCQ = 1
    QUESTION_TYPE_DESCRIPTIVE = 2
    QUESTION_TYPE_FILE = 3
    QUESTION_TYPE_CHOICES = (
        (QUESTION_TYPE_MCQ, "MCQ"),
        (QUESTION_TYPE_DESCRIPTIVE, "Descriptive"),
        (QUESTION_TYPE_FILE, "File"),
    )

    title = models.TextField()
    question_type = models.PositiveSmallIntegerField(default=QUESTION_TYPE_DESCRIPTIVE,
                                                     choices=QUESTION_TYPE_CHOICES)

    exams = models.ManyToManyField(Exam)

    def __str__(self):
        return f'{self.question_type} - {self.title[:25]}'


class McqChoices(models.Model):
    value = models.PositiveSmallIntegerField()

    question = models.ForeignKey(Question, on_delete=models.CASCADE)


class Submission(models.Model):
    submitted_at = models.DateTimeField(default=timezone.now)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.submitted_at


class Answer(models.Model):
    value = models.TextField()

    submission = models.ForeignKey(Submission, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.question}: {self.value}'
