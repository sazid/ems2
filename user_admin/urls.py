from django.urls import path

from user_admin import views

urlpatterns = [
    path('', views.home, name='user_admin-home'),
    path('university/', views.UniversityListView.as_view(), name='user_admin-university-list'),
]
