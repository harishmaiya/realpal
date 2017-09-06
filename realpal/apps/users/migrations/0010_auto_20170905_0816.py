# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-09-05 15:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20170828_0734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='house_cond',
            field=models.SmallIntegerField(blank=True, choices=[(0, 'Move-in ready'), (1, 'Slightly dated'), (2, 'Fixer Upper')], null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='house_type',
            field=models.SmallIntegerField(blank=True, choices=[(0, 'Single Family'), (1, 'Town home'), (2, 'Condominium'), (5, 'Flexible')], null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='purchase_step',
            field=models.SmallIntegerField(choices=[(0, 'Decide and Prepare'), (1, 'Evaluate and Offer'), (2, 'House owning')], default=0),
        ),
        migrations.AlterField(
            model_name='user',
            name='status',
            field=models.SmallIntegerField(blank=True, choices=[(0, "Good locality, schools doesn't matter"), (2, 'School district upcoming'), (3, 'Need established schools'), (4, 'Investment, rent')], null=True),
        ),
    ]