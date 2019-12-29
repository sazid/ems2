from distutils import command

from django.shortcuts import render, redirect

from core.models import University
from users.forms import UserRegistrationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from users.models import User


def user_registration_view(request):
    # Students can create their own accounts
    user_role = User.STUDENT

    if request.user.is_authenticated:
        if request.user.role == User.ADMIN:
            # Admins can create University Admin accounts
            user_role = User.UNIVERSITY_ADMIN
        elif request.user.role == User.UNIVERSITY_ADMIN:
            # University Admins can create Faculty accounts
            user_role = User.FACULTY

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            # Set user role
            user.role = user_role
            user.save()

            # Set university for faculty users
            if request.user.role == User.UNIVERSITY_ADMIN:
                for uni in request.user.university_set.all():
                    user.university_set.add(uni)
                user.save()

            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')

            return redirect('core-home')
        else:
            messages.error(request, 'Failed to create account!')
    else:
        form = UserRegistrationForm(initial={'role': user_role})

    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'users/profile.html')
