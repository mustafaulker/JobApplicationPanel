# Generated by Django 4.1.2 on 2022-11-04 18:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicationModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position_id', models.IntegerField()),
                ('applicant_id', models.IntegerField()),
                ('application_date', models.DateField(default=datetime.datetime(1970, 1, 1, 0, 0), max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='PositionModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position_title', models.CharField(max_length=100)),
                ('position_location', models.CharField(max_length=100)),
                ('position_salary', models.IntegerField(default=0)),
            ],
        ),
    ]