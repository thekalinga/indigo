# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-11-09 17:17
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('indigo_api', '0030_annotation'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocumentActivity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nonce', models.CharField(max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('document', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='activities', to='indigo_api.Document')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='document_activities', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='documentactivity',
            unique_together=set([('document', 'user', 'nonce')]),
        ),
    ]
