from django.shortcuts import render, redirect
from django.http import HttpResponse
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
