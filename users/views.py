from django.shortcuts import render, redirect
from users.forms import UserRegistrationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from users.models import User


def student_registration_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            # Save this user as a student
            form.role = User.STUDENT
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now log in.')
            return redirect('users-login')
        else:
            messages.error(request, 'Failed to create account!')
    else:
        form = UserRegistrationForm()

    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'users/profile.html')
