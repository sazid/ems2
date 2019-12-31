from django.urls import path

from core.views import core
from user_uni_admin import views

urlpatterns = [
    path('course/', views.CourseListView.as_view(), name='user_uni_admin-course-list'),
    path('course/<int:pk>/', views.CourseDetailView.as_view(), name='user_uni_admin-course-detail'),
    path('course/new/', views.CourseCreateView.as_view(), name='user_uni_admin-course-create'),
    path('course/<int:pk>/update/', views.CourseUpdateView.as_view(), name='user_uni_admin-course-update'),

    path('faculty/', views.FacultyListView.as_view(), name='user_uni_admin-faculty-list'),
]
