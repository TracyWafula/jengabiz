# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-16 22:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('product', models.CharField(max_length=650)),
                ('quantity', models.IntegerField(default=0)),
                ('unit', models.FloatField(default=0)),
                ('unit_price', models.FloatField(default=0)),
                ('amount', models.FloatField(default=0)),
            ],
        ),
    ]
