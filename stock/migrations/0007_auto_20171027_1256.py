# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-27 09:56
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0006_auto_20171027_1246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 27, 9, 56, 10, 386583, tzinfo=utc)),
        ),
    ]
