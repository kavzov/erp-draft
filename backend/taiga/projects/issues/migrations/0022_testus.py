# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-26 15:42
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0021_auto_20170626_1503'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('testus', django.contrib.postgres.fields.jsonb.JSONField()),
            ],
        ),
    ]
