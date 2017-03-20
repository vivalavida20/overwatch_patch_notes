# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-20 14:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('patch_app', '0003_auto_20170320_2317'),
    ]

    operations = [
        migrations.CreateModel(
            name='PatchNotes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('subject', models.CharField(max_length=100)),
                ('text', models.TextField()),
                ('patch_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='TestPatchNotes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('subject', models.CharField(max_length=100)),
                ('text', models.TextField()),
                ('patch_date', models.DateTimeField()),
            ],
        ),
    ]
