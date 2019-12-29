from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
)

from core.models import University
from users.models import User

from user_admin import forms


def uni_admin_test_func(self):
    """
    Tests to check whether the user is a university admin or not
    :param self: self parameter from inside the class
    :return: True if the user is admin
    """

    if self.request.user.role == User.UNIVERSITY_ADMIN:
        return True
    return False


class UniversityListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = University
    template_name = 'user_admin/university_list.html'
    ordering = ['name']

    test_func = uni_admin_test_func


class UniversityDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = University
    template_name = 'user_admin/university_detail.html'

    def get_context_data(self, **kwargs):
        context = super(UniversityDetailView, self).get_context_data(**kwargs)
        context['university_admins'] = User.objects.filter(role=User.UNIVERSITY_ADMIN, university=self.object)
        return context

    test_func = uni_admin_test_func


class UniversityCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = University
    template_name = 'user_admin/university_form.html'
    form_class = forms.UniversityCreateForm

    test_func = uni_admin_test_func


class UniversityUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = University
    template_name = 'user_admin/university_form.html'
    form_class = forms.UniversityCreateForm

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
