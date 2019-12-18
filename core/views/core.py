from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    # return HttpResponse('test')
    return render(request, 'core/home.html')


def about(request):
    return render(request, 'core/about.html', {'title': 'About'})
