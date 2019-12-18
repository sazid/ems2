from django import forms
from django.contrib.auth.forms import UserCreationForm

from users.models import User

class UserRegistrationForm(UserCreationForm):
    # email = forms.EmailField(max_length=250, help_text='Required. Add a valid email address')

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'first_name', 'last_name', 'email', 'role',)
