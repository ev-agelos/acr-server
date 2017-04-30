# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-30 11:59
from __future__ import unicode_literals

from django.db import migrations, models

def set_my_defaults(apps, schema_editor):
    Laptime = apps.get_model('laptimes', 'Laptime')
    for laptime in Laptime.objects.all().iterator():
        laptime.updated_as = sum(laptime.splits)
        laptime.save()

class Migration(migrations.Migration):

    dependencies = [
        ('laptimes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='laptime',
            name='time',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.RunPython(set_my_defaults),
        migrations.AlterField(
            model_name='laptime',
            name='time',
            field=models.PositiveIntegerField(),
        ),
    ]
