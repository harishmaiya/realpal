# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-04 15:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20170804_0108'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='home_type',
        ),
        migrations.AddField(
            model_name='user',
            name='house_age',
            field=models.CharField(blank=True, choices=[('SF', 'Single Family'), ('TH', 'Townhome'), ('CN', 'Condominium'), ('NC', 'New Construction'), ('OT', 'Other Options'), ('FX', 'Flexible')], max_length=3),
        ),
        migrations.AddField(
            model_name='user',
            name='house_cond',
            field=models.CharField(blank=True, choices=[('UP', 'Updated'), ('SL', 'Slightly dated'), ('FU', 'Fixer Upper')], max_length=3),
        ),
        migrations.AddField(
            model_name='user',
            name='house_type',
            field=models.CharField(blank=True, choices=[('SF', 'Single Family'), ('TH', 'Townhome'), ('CN', 'Condominium'), ('NC', 'New Construction'), ('OT', 'Other Options'), ('FX', 'Flexible')], max_length=2),
        ),
        migrations.AlterField(
            model_name='user',
            name='credit_score',
            field=models.CharField(blank=True, choices=[('780+', '780+'), ('740-779', '740-779'), ('700-739', '700-739'), ('650-699', '650-699'), ('600-649', '600-649'), ('<599', '<599')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='status',
            field=models.CharField(choices=[('SI', 'Single'), ('MNK', 'Married with No Kids'), ('MNSK', 'Married with No School Kids'), ('MSK', 'Married with School Kids'), ('INV', 'Investor')], default='SI', max_length=4),
        ),
    ]
