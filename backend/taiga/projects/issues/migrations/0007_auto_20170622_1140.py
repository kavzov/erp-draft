# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-22 11:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0006_auto_20170622_0902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='assigned_to',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='issues', to='users.User'),
        ),
    ]
