# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-27 20:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0007_auto_20171027_1256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
