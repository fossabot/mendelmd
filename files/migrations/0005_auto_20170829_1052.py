# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-29 10:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0004_auto_20170824_1500'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='size',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]