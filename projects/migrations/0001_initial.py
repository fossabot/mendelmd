# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-06 23:41
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('files', '__first__'),
        ('auth', '0008_alter_user_username_max_length'),
        ('individuals', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField(blank=True, null=True)),
                ('is_public', models.BooleanField(default=False)),
                ('status', models.CharField(blank=True, editable=False, max_length=100)),
                ('creation_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified_date', models.DateTimeField(blank=True, null=True)),
                ('files', models.ManyToManyField(blank=True, to='files.File')),
                ('groups', models.ManyToManyField(blank=True, related_name='project_groups', to='auth.Group')),
                ('individuals', models.ManyToManyField(blank=True, to='individuals.Individual')),
                ('members', models.ManyToManyField(blank=True, related_name='project_members', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]