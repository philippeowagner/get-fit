# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2018-01-13 04:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('counter', '0002_auto_20180112_2159'),
    ]

    operations = [
        migrations.AddField(
            model_name='goal',
            name='isActive',
            field=models.BooleanField(default=False),
        ),
    ]
