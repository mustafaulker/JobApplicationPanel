from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.shortcuts import render, redirect

from .forms import PositionForm
from .models import PositionModel


def positions(request):
    return render(request, "positions.html", {'positions': PositionModel.objects.all()})


def add_position(request):
    if request.method == 'POST':
        form = PositionForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('positions')
    else:
        form = PositionForm()

    return render(request, "JAP/add_position.html", {'form': form})


def registered_users(request):
    return render(request, "JAP/registered_users.html",
                  {'registered_users': Group.objects.get(name="User").user_set.all()})


@login_required
def profile(request):
    return render(request, "profile.html",
                  {'registered_users': Group.objects.get(name="User").user_set.all()})
