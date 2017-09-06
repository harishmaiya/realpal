# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-09-06 05:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_auto_20170905_2216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='house_age',
            field=models.SmallIntegerField(blank=True, choices=[(0, 'New Construction'), (1, 'One to fifteen'), (3, 'Over sixteen')], null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='status',
            field=models.SmallIntegerField(blank=True, choices=[(0, "Convenience, schools doesn't matter much"), (2, 'Upcoming school district'), (3, 'Need established schools'), (4, 'Investment/rent')], null=True),
        ),
    ]
