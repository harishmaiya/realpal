# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-21 07:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20170821_0005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='preferred_city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='realpal.apps.users.City'),
        ),
    ]
