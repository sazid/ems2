from django import forms

from users.models import User
from core.models import Course


class CourseCreateForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('name', 'code', 'is_active', 'university',)

    # def __init__(self, *args, **kwargs):
    #     super(CourseCreateForm, self).__init__(*args, **kwargs)
    #     self.fields['users'].queryset = User.objects.filter(role=User.UNIVERSITY_ADMIN)
