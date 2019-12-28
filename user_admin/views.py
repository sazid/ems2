from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
)

from core.models import University
from users.models import User

from user_admin import forms


class UniversityListView(ListView):
    model = University
    template_name = 'user_admin/university_list.html'
    ordering = ['name']


class UniversityDetailView(DetailView):
    model = University
    template_name = 'user_admin/university_detail.html'

    def get_context_data(self, **kwargs):
        context = super(UniversityDetailView, self).get_context_data(**kwargs)
        context['university_admins'] = User.objects.filter(role=User.UNIVERSITY_ADMIN, university=self.object)
        return context


class UniversityCreateView(CreateView):
    model = University
    template_name = 'user_admin/university_form.html'
    form_class = forms.UniversityCreateForm


class UniversityUpdateView(UpdateView):
    model = University
    template_name = 'user_admin/university_form.html'
    form_class = forms.UniversityCreateForm
