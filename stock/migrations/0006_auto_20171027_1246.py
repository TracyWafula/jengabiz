# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-27 09:46
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0005_auto_20171027_1239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 27, 9, 46, 1, 877309, tzinfo=utc)),
        ),
    ]
