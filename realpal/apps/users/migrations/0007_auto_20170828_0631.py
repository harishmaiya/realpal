# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-28 13:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20170828_0051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='firsthome',
            field=models.BooleanField(default=True),
        ),
    ]
