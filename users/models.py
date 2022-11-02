from datetime import datetime

from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import ArrayField
from django.db import models


class CustomUser(AbstractUser):
    interests = ArrayField(models.CharField(max_length=30, blank=True, default=''), default=list)
    date_of_birth = models.DateField(max_length=8, default=datetime(1970, 1, 1))
    location = models.CharField(max_length=30, default='Istanbul')
    title = models.CharField(max_length=40, default='Senior Software Architect')
