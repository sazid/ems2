from django.utils import timezone
from django.db import models
from users.models import User
from django.urls import reverse


class University(models.Model):
    name = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    is_active = models.BooleanField(default=True)
    website = models.URLField(blank=True, default='')
    description = models.TextField(blank=True, default='')

    users = models.ManyToManyField(User)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('user_admin-university-detail', kwargs={'pk': self.pk})


class Course(models.Model):
    name = models.CharField(max_length=500)
    code = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)

    university = models.ForeignKey(University, on_delete=models.CASCADE)

    def __str__(self):
        return f'[{self.code}] {self.name}'

    def get_absolute_url(self):
        return reverse('user_uni_admin-course-detail', kwargs={'pk': self.pk})


class Exam(models.Model):
    name = models.CharField(max_length=500)
    start = models.DateTimeField()
    end = models.DateTimeField()
    note = models.TextField()

    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} {self.course}'

    def is_ongoing(self):
        return self.start <= timezone.now() <= self.end

    def is_previous(self):
        return self.start <= self.end < timezone.now()

    def is_upcoming(self):
        return self.end >= self.start > timezone.now()


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


class Submission(models.Model):
    submitted_at = models.DateTimeField(default=timezone.now)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user} at {self.submitted_at}'


class Answer(models.Model):
    value = models.TextField()

    submission = models.ForeignKey(Submission, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.question}: {self.value}'
