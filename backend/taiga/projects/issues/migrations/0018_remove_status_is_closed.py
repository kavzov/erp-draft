# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-26 14:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0017_auto_20170626_1438'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='status',
            name='is_closed',
        ),
    ]
