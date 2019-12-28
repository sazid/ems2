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


def home(request):
    return render(request, 'user_admin/home.html')


class UniversityListView(ListView):
    model = University
    template_name = 'user_admin/university_list.html'
