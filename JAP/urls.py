from django.urls import path

from . import views

urlpatterns = [
    path('positions', views.positions, name='positions'),
    path('add_position', views.add_position, name='add_position'),
    path('registered_users', views.registered_users, name='registered_users'),
    path('profile', views.profile, name='profile'),
    path('edit_profile', views.edit_profile, name='edit_profile'),
    path('edit_interests', views.edit_interests, name='edit_interests'),
]
