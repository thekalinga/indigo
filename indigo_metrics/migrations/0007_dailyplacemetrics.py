# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-09-01 13:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('indigo_api', '0110_django3_tweaks'),
        ('indigo_metrics', '0006_auto_20190901_1340'),
    ]

    operations = [
        migrations.CreateModel(
            name='DailyPlaceMetrics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(db_index=True)),
                ('place_code', models.CharField(db_index=True, max_length=20)),
                ('n_activities', models.IntegerField(default=0)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='indigo_api.Country')),
                ('locality', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='indigo_api.Locality')),
            ],
            options={
                'db_table': 'indigo_metrics_daily_placemetrics',
            },
        ),
        migrations.AlterUniqueTogether(
            name='dailyplacemetrics',
            unique_together=set([('date', 'place_code')]),
        ),
    ]
