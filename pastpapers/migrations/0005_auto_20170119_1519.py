# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-01-19 12:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pastpapers', '0004_paper_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paper',
            name='unit',
        ),
        migrations.AddField(
            model_name='paper',
            name='unit_code',
            field=models.CharField(choices=[('SMA 2270', 'SMA 2270'), ('EGS 2304', 'EGS 2304')], default='SMA', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='paper',
            name='unit_title',
            field=models.CharField(choices=[('calculus_1', 'Calculus 1'), ('calculus_2', 'Calculus 2'), ('calculus_3', 'calculus 3'), ('calculus_4', 'calculus 4')], default='CALCULUS', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='paper',
            name='year',
            field=models.CharField(choices=[('first-year', 'First Year'), ('second-year', 'Second Year'), ('third-year', 'Third Year'), ('fourth-year', 'Fourth Year'), ('fifth-year', 'Fifth Year')], max_length=50),
        ),
        migrations.DeleteModel(
            name='Unit',
        ),
    ]