# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-20 15:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=250)),
                ('text', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=250)),
                ('posted_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('parent_id', models.IntegerField(db_index=True, default=0)),
                ('articles_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='commentApp.Articles')),
            ],
        ),
    ]
