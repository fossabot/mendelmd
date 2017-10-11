# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-01 10:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('type', models.CharField(max_length=30)),
                ('status', models.CharField(max_length=30)),
                ('worker_id', models.CharField(max_length=30)),
                ('ip', models.CharField(max_length=30)),
                ('creation_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified_date', models.DateTimeField(blank=True, null=True)),
                ('started', models.DateTimeField(null=True)),
                ('finished', models.DateTimeField(null=True)),
                ('execution_time', models.TimeField(null=True)),
            ],
        ),
    ]