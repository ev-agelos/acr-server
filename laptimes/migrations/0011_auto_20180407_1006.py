# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-07 10:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('laptimes', '0010_auto_20180322_0701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laptime',
            name='car_setup',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='laptimes.CarSetup'),
        ),
    ]
