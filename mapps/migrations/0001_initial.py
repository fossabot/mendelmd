# Generated by Django 2.0.2 on 2018-03-05 15:50

from django.conf import settings
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='App',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('status', models.CharField(max_length=255)),
                ('category', models.CharField(max_length=255)),
                ('source', models.CharField(blank=True, max_length=600, null=True)),
                ('repository', models.CharField(blank=True, max_length=600, null=True)),
                ('install', models.CharField(blank=True, max_length=600, null=True)),
                ('main', models.CharField(blank=True, max_length=600, null=True)),
                ('type', models.CharField(max_length=255)),
                ('config', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('user', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
