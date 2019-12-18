from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from users.forms import UserRegistrationForm
from django.contrib import messages


def registration_view(request):

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('core-home')
        else:
            messages.error(request, 'Failed to create account!')
    else:
        form = UserRegistrationForm()

    return render(request, 'users/register.html', {'form': form})
