# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-03 12:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sale', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
