from django.urls import path

from core.views import core

urlpatterns = [
    path('', core.home, name='core-home'),
    path('about/', core.about, name='core-about'),
]
