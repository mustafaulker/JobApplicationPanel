from django.urls import path

from .views import signup, hr_signup, password_reset


urlpatterns = [
    path('signup/', signup, name='signup'),
    path('hr_signup/', hr_signup, name='hr_signup'),
    path('password_reset/', password_reset, name='password_reset'),
]
