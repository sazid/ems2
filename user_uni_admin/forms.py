from django import forms

from users.models import User
from core.models import University


class UniversityCreateForm(forms.ModelForm):
    class Meta:
        model = University
        fields = ('name', 'email', 'website', 'description', 'is_active', 'users',)

    def __init__(self, *args, **kwargs):
        super(UniversityCreateForm, self).__init__(*args, **kwargs)
        self.fields['users'].queryset = User.objects.filter(role=User.UNIVERSITY_ADMIN)
