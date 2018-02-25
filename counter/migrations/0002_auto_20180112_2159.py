# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2018-01-13 02:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('counter', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meal',
            name='units',
            field=models.CharField(choices=[('grams', 'Grams'), ('ounces', 'Ounces'), ('kilograms', 'KIlograms'), ('pounds', 'Pounds'), ('milliliters', 'Milliliters'), ('liters', 'Liters'), ('cup', 'Cup'), ('scoop', 'Scoop'), ('piece', 'Piece'), ('can', 'Can')], default='grams', max_length=15),
        ),
    ]