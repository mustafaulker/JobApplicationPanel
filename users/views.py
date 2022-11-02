from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import Group
from django.shortcuts import render, redirect

from .forms import SignUpForm, HRSignUpForm

user_group, created = Group.objects.get_or_create(name="User")
hr_group, created = Group.objects.get_or_create(name="HR")


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.password = make_password(form.cleaned_data['password'])
            user.save()
            user_group.user_set.add(user)
            return redirect('positions')
    else:
        form = SignUpForm()
    return render(request, "registration/signup.html", {'form': form})


def hr_signup(request):
    if request.method == 'POST':
        form = HRSignUpForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.password = make_password(form.cleaned_data['password'])
            user.save()
            hr_group.user_set.add(user)
            return redirect('positions')
    else:
        form = HRSignUpForm()
    return render(request, "registration/hr_signup.html", {'form': form})


@login_required
def password_reset(request):
    user = request.user
    if request.method == 'POST':
        form = SetPasswordForm(user, request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your password has been changed")
            return redirect('login')
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)

    form = SetPasswordForm(user)
    return render(request, 'registration/password_reset.html', {'form': form})
