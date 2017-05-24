# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-24 08:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        ('projects', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=128)),
                ('description', models.TextField(max_length=1024)),
                ('assigned_to', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='users.User')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='projects.Project')),
            ],
            options={
                'verbose_name_plural': 'issues',
                'verbose_name': 'issue',
                'ordering': ['id'],
            },
        ),
    ]
