from django.shortcuts import redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.urls import reverse
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
)

from core.models import Exam, Course, University
from users.models import User

from user_uni_admin import forms


def student_test_func(self):
    """
    Tests to check whether the user is a student
    :param self: self parameter from inside the class
    :return: True if the user is admin
    """

    if self.request.user.role == User.STUDENT:
        return True
    return False


class CourseListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Course
    template_name = 'user_student/course_list.html'

    def get_queryset(self):
        return Course.objects.filter(
            university=self.request.user.university_set.first()
        ).order_by('name')

    test_func = student_test_func


class ExamListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Exam
    template_name = 'user_student/exam_list.html'

    def get_queryset(self):
        return Exam.objects.filter(
            course_id=self.kwargs['pk'],
        )

    test_func = student_test_func


class CourseDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Course
    template_name = 'user_uni_admin/course_detail.html'

    test_func = student_test_func
