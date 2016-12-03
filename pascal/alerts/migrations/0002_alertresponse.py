# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-30 03:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alerts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AlertResponse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField()),
                ('alerts', models.ManyToManyField(to='alerts.Alert')),
            ],
        ),
    ]
