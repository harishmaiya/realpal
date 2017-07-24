# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-24 16:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('state', models.CharField(max_length=40)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='annual_income',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='budget',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='credit_score',
            field=models.CharField(blank=True, choices=[('780+', '780+'), ('740-779', '740-779'), ('700-739', '700-739'), ('660-699', '600-699'), ('600-659', '600-659'), ('<599', '<599')], max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='current_rent',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='home_type',
            field=models.CharField(blank=True, choices=[('SF', 'Single Family'), ('TH', 'Townhome'), ('CN', 'Condonomiums'), ('O', 'Other Options')], max_length=2),
        ),
        migrations.AddField(
            model_name='user',
            name='language',
            field=models.CharField(choices=[('EN', 'English'), ('ESP', 'Spanish'), ('CA', 'Mandarin/Cantonese'), ('HI', 'Hindi'), ('OT', 'Other')], default='EN', max_length=2),
        ),
        migrations.AddField(
            model_name='user',
            name='status',
            field=models.CharField(choices=[('SI', 'Single'), ('MNK', 'Married with No Kids'), ('MNSK', 'Married with No School Kids'), ('MSK', 'Married with School Kids')], default='SI', max_length=4),
        ),
        migrations.AddField(
            model_name='user',
            name='interested_cities',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='interested_users', to='users.City'),
        ),
    ]
