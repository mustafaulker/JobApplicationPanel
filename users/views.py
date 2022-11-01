from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, SetPasswordForm
from django.contrib.auth.models import Group
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic

user_group, created = Group.objects.get_or_create(name="User")
hr_group, created = Group.objects.get_or_create(name="HR")


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = "registration/signup.html"

    def form_valid(self, form):
        user = form.save()
        user_group.user_set.add(user)
        return super().form_valid(form)


class HRSignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = "registration/hr_signup.html"

    def form_valid(self, form):
        form.instance.is_staff = True
        user = form.save()
        hr_group.user_set.add(user)
        return super().form_valid(form)


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
