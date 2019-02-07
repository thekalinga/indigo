# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-12-07 09:25
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_fsm


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('indigo_api', '0077_work_publication_document'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('description', models.TextField(blank=True, null=True)),
                ('anchor_id', models.CharField(blank=True, max_length=128, null=True)),
                ('state', django_fsm.FSMField(default=b'open', max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('assigned_to', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='assigned_tasks', to=settings.AUTH_USER_MODEL)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='indigo_api.Country')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('document', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='indigo_api.Document')),
                ('locality', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='indigo_api.Locality')),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('work', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='indigo_api.Work')),
            ],
            options={
                'permissions': (('submit_task', 'Can submit an open task for review'), ('cancel_task', 'Can cancel a task that is open or has been submitted for review'), ('reopen_task', 'Can reopen a task that is closed or cancelled'), ('unsubmit_task', 'Can reopen a task that has been submitted for review'), ('close_task', 'Can close a task that has been submitted for review')),
            },
        ),
        migrations.CreateModel(
            name='Workflow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('description', models.TextField(blank=True, null=True)),
                ('tasks', models.ManyToManyField(related_name='workflows', to='indigo_api.Task')),
            ],
        ),
    ]