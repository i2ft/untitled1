# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-13 18:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='start_date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='start_time',
            field=models.TimeField(auto_now=True),
        ),
    ]