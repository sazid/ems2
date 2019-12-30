from django.urls import path

from core.views import core
from user_uni_admin import views

urlpatterns = [
    path('course/', views.CourseListView.as_view(), name='user_uni_admin-course-list'),
    # path('university/<int:pk>/', views.UniversityDetailView.as_view(), name='user_admin-university-detail'),
    # path('university/new/', views.UniversityCreateView.as_view(), name='user_admin-university-create'),
    # path('university/<int:pk>/update/', views.UniversityUpdateView.as_view(), name='user_admin-university-update'),
    #
    path('faculty/', views.FacultyListView.as_view(), name='user_uni_admin-faculty-list'),
]
