from django.urls import path

from .views import SignUpView, HRSignUpView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('hr_signup/', HRSignUpView.as_view(), name='hr_signup'),
]
