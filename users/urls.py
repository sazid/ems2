from django.urls import path
from django.contrib.auth import views as auth_views

import users.views as user_views

urlpatterns = [
    path('register/', user_views.student_registration_view, name='users-register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='users-login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='users-logout'),
]
