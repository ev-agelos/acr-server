# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-05 13:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('laptimes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='track',
            old_name='name',
            new_name='circuit',
        ),
    ]
