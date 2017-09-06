# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-09-06 05:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_auto_20170905_0816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='house_age',
            field=models.SmallIntegerField(blank=True, choices=[(0, 'New Construction'), (1, 'One to Fifteen'), (3, 'Over thirty')], null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='status',
            field=models.SmallIntegerField(blank=True, choices=[(0, "Convenience, schools doesn't matter much"), (2, 'Upcoming school district'), (3, 'Need established schools'), (4, 'Investment, rent')], null=True),
        ),
    ]
