# Generated by Django 2.0.1 on 2018-01-08 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_path'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='path',
            name='project',
        ),
        migrations.AddField(
            model_name='project',
            name='paths',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='Path',
        ),
    ]