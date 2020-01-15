from django.urls import path

from core.views import core
from user_student import views

urlpatterns = [
    path('course/', views.CourseListView.as_view(), name='user_student-course-list'),
    path('course/<int:pk>/exam/', views.ExamListView.as_view(), name='user_student-exam-list'),
    path('exam/<int:pk>/submission/new/', views.CourseDetailView.as_view(), name='user_student-new-submission'),
]
