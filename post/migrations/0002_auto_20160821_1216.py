# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-21 03:16
from __future__ import unicode_literals

from django.db import migrations, models
import markdownx.models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='myfield',
        ),
        migrations.AddField(
            model_name='post',
            name='dep',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=markdownx.models.MarkdownxField(),
        ),
        migrations.AlterField(
            model_name='post',
            name='parent',
            field=models.CharField(default='NULL', max_length=24),
        ),
    ]