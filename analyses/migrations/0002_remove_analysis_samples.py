# Generated by Django 2.0.1 on 2018-02-12 19:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('analyses', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='analysis',
            name='samples',
        ),
    ]