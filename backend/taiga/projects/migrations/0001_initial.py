# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-24 08:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('description', models.TextField(max_length=1024)),
            ],
            options={
                'verbose_name_plural': 'projects',
                'ordering': ['id'],
                'verbose_name': 'project',
            },
        ),
    ]