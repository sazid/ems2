from django import forms
from django.contrib.auth.forms import UserCreationForm

from core.models import University
from users.models import User


class UserRegistrationForm(UserCreationForm):
    def __init__(self, user, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        if user and user.is_authenticated:
            self.fields['university'] = forms.ModelChoiceField(
                queryset=University.objects.filter(users__in=[user])
            )
        elif user == False:
            self.fields['university'] = forms.ModelChoiceField(
                queryset=University.objects.all()
            )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'first_name', 'last_name',)
