# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-08 09:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('indigo_api', '0072_import_locality_from_indigo_app'),
    ]

    operations = [
        migrations.AlterField(
            model_name='locality',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='localities', to='indigo_api.Country'),
        ),
    ]
