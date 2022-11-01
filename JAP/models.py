from django.db import models


class PositionModel(models.Model):
    title = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    salary = models.IntegerField()

    def __str__(self):
        return self.title
