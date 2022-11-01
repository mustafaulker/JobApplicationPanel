from django.urls import path

from . import views

urlpatterns = [
    path('positions', views.positions, name='positions'),
    path('add_position', views.add_position, name='add_position'),
]
