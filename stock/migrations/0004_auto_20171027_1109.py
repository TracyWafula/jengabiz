# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-27 08:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0003_auto_20171027_1101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='unit',
            field=models.IntegerField(default=0),
        ),
    ]