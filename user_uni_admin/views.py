from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
)

from core.models import Course
from users.models import User

from user_uni_admin import forms


def uni_admin_test_func(self):
    """
    Tests to check whether the user is a university admin or not
    :param self: self parameter from inside the class
    :return: True if the user is admin
    """

    if self.request.user.role == User.UNIVERSITY_ADMIN:
        return True
    return False


class CourseListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Course
    template_name = 'user_uni_admin/course_list.html'

    def get_queryset(self):
        return Course.objects.filter(
            university=self.request.user.university_set.first()
        ).order_by('name')

    test_func = uni_admin_test_func


class CourseDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Course
    template_name = 'user_uni_admin/course_detail.html'

    test_func = uni_admin_test_func


class CourseCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Course
    template_name = 'user_uni_admin/course_form.html'
    form_class = forms.CourseCreateForm

    test_func = uni_admin_test_func


class CourseUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Course
    template_name = 'user_uni_admin/course_form.html'
    form_class = forms.CourseCreateForm

    test_func = uni_admin_test_func


class FacultyListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = User
    template_name = 'user_uni_admin/faculty_list.html'

    def get_queryset(self):
        return User.objects.filter(
            role=User.FACULTY,
            university__in=self.request.user.university_set.all()
        ).order_by('first_name').distinct()

    test_func = uni_admin_test_func
