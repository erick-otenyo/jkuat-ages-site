# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-01-19 20:06
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='activity',
            options={'verbose_name_plural': 'activities'},
        ),
        migrations.AddField(
            model_name='activity',
            name='category',
            field=models.CharField(choices=[('normal', 'normal'), ('notice', 'notice')], default='normal', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='activity',
            name='location',
            field=django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326),
        ),
        migrations.AlterField(
            model_name='activity',
            name='slug',
            field=models.SlugField(unique_for_date='date'),
        ),
    ]
