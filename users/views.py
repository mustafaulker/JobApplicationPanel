from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from django.urls import reverse_lazy
from django.views import generic

applicant_group, created = Group.objects.get_or_create(name="Applicant")
hr_group, created = Group.objects.get_or_create(name="HR")


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = "registration/signup.html"

    def form_valid(self, form):
        user = form.save()
        applicant_group.user_set.add(user)
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
