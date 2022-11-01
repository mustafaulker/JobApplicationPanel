from django.urls import path

from .views import SignUpView, HRSignUpView
from . import views

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('hr_signup/', HRSignUpView.as_view(), name='hr_signup'),
    path('password_reset/', views.password_reset, name='password_reset'),
]
