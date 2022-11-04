from django.contrib import admin

from .models import PositionModel, ApplicationModel

admin.site.register(PositionModel)
admin.site.register(ApplicationModel)
