from datetime import datetime

from django.db import models


class PositionModel(models.Model):
    position_title = models.CharField(max_length=100)
    position_location = models.CharField(max_length=100)
    position_salary = models.IntegerField(default=0)

    def __str__(self):
        return self.position_title


class ApplicationModel(models.Model):
    position_id = models.IntegerField()
    applicant_id = models.IntegerField()
    application_date = models.DateField(max_length=8, default=datetime(1970, 1, 1))
