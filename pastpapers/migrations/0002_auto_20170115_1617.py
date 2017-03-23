# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-01-15 13:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pastpapers', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paper',
            name='year',
        ),
        migrations.AddField(
            model_name='unit',
            name='year',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='pastpapers.Year'),
            preserve_default=False,
        ),
    ]
