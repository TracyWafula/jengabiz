# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-03 19:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0003_remove_expenses_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='expenses',
            name='sum',
            field=models.FloatField(default=0),
        ),
    ]
