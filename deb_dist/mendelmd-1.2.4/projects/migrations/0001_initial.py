# Generated by Django 2.1.4 on 2018-12-27 08:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('files', '__first__'),
        ('auth', '0009_alter_user_last_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('individuals', '__first__'),
        ('tasks', '__first__'),
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
                ('paths', models.TextField(blank=True, null=True)),
                ('creation_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified_date', models.DateTimeField(blank=True, null=True)),
                ('files', models.ManyToManyField(blank=True, to='files.File')),
                ('groups', models.ManyToManyField(blank=True, related_name='project_groups', to='auth.Group')),
                ('individuals', models.ManyToManyField(blank=True, to='individuals.Individual')),
                ('members', models.ManyToManyField(blank=True, related_name='project_members', to=settings.AUTH_USER_MODEL)),
                ('tasks', models.ManyToManyField(blank=True, to='tasks.Task')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.TextField(blank=True, null=True)),
                ('name', models.CharField(max_length=300)),
                ('size', models.BigIntegerField(blank=True, null=True)),
                ('human_size', models.CharField(max_length=300)),
                ('last_modified', models.DateTimeField(blank=True, null=True)),
                ('file_type', models.TextField(blank=True, null=True)),
                ('status', models.CharField(max_length=300)),
                ('md5', models.TextField(blank=True, null=True)),
                ('creation_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified_date', models.DateTimeField(blank=True, null=True)),
                ('project', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='projects.Project')),
                ('user', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectSample',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('alias', models.CharField(max_length=300)),
                ('status', models.CharField(blank=True, max_length=300)),
                ('location', models.TextField(blank=True, null=True)),
                ('prefix', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('comments', models.TextField(blank=True, null=True)),
                ('creation_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified_date', models.DateTimeField(auto_now=True, null=True)),
                ('last_modified', models.DateTimeField(blank=True, null=True)),
                ('n_files', models.IntegerField(blank=True, default=0, null=True)),
                ('n_fastqs', models.IntegerField(blank=True, default=0, null=True)),
                ('n_bams', models.IntegerField(blank=True, default=0, null=True)),
                ('n_vcfs', models.IntegerField(blank=True, default=0, null=True)),
                ('files', models.ManyToManyField(blank=True, to='projects.ProjectFile')),
                ('project', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='projects.Project')),
                ('user', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]