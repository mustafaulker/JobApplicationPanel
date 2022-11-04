from datetime import datetime

from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.shortcuts import render, redirect

from users.models import CustomUser
from .forms import PositionForm
from .models import PositionModel, ApplicationModel


@login_required
def positions(request):
    if request.method == 'POST' and 'delete_position' in request.POST:
        PositionModel.objects.filter(id=request.POST.get('delete_position')).delete()
    elif request.method == 'POST' and 'apply_position' in request.POST:

        ApplicationModel.objects.create(
            position_id=int(request.POST.get('apply_position')),
            applicant_id=int(request.user.id),
            application_date=datetime.now().date()
        ).save()
    return render(request, "positions.html", {'positions': PositionModel.objects.all()})


@staff_member_required
def add_position(request):
    if request.method == 'POST':
        form = PositionForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('positions')
    else:
        form = PositionForm()

    return render(request, "JAP/add_position.html", {'form': form})


@staff_member_required
def registered_users(request):
    if request.method == 'POST':
        get_user_model().objects.filter(id=request.POST.get('reg_user_id')).delete()
    return render(request, "JAP/registered_users.html",
                  {'registered_users': Group.objects.get(name="User").user_set.all()})


@login_required
def profile(request):
    return render(request, "profile.html", {'current_user': request.user})


@login_required
def edit_profile(request):
    if request.method == 'POST':
        request.user.first_name = request.POST['new_first_name']
        request.user.last_name = request.POST['new_last_name']
        request.user.email = request.POST['new_email']
        request.user.location = request.POST['new_location']
        request.user.title = request.POST['new_title']
        request.user.date_of_birth = datetime.strptime(request.POST['new_date_of_birth'], '%Y-%m-%d')

        request.user.save()

        return redirect('profile')

    return render(request, "JAP/edit_profile.html", {'current_user': request.user})


@login_required
def edit_interests(request):
    if request.method == 'POST' and 'delete_interest' in request.POST:
        request.user.interests.remove(request.POST['delete_interest'])
        request.user.save()

    elif request.method == 'POST' and 'add_interest' in request.POST:
        new_interest = request.POST['add_interest']
        request.user.interests.append(new_interest)
        request.user.save()

    return render(request, "JAP/edit_interests.html", {'current_user': request.user})


@login_required
def job_applications(request):
    def map_applications(app_obj):
        position_obj = PositionModel.objects.get(id=app_obj.position_id)
        user_obj = CustomUser.objects.get(id=app_obj.applicant_id)
        application_date = app_obj.application_date
        application_id = app_obj.id
        return user_obj, position_obj, application_date, application_id

    applications_map = map(map_applications, ApplicationModel.objects.all())

    if request.method == 'POST':
        ApplicationModel.objects.get(id=request.POST['application_id']).delete()
        return redirect(job_applications)

    return render(request, 'JAP/job_applications.html', {'applications_map': applications_map})
