# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-04 16:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('individuals', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='individual',
            name='location',
            field=models.TextField(blank=True, null=True),
        ),
    ]