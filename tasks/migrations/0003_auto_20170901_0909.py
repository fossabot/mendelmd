# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-01 09:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_auto_20170901_0908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='execution_time',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='finished',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='started',
            field=models.DateTimeField(null=True),
        ),
    ]
