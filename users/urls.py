from django.urls import path

import users.views as user_views

urlpatterns = [
    path('register/', user_views.student_registration_view, name='users-register'),
]
