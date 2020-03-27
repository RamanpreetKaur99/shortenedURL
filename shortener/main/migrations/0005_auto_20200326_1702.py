# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2020-03-26 17:02
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20200326_1637'),
    ]

    operations = [
        migrations.AddField(
            model_name='database',
            name='length',
            field=models.IntegerField(default=15, validators=[django.core.validators.MinValueValidator(10), django.core.validators.MaxValueValidator(20)]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='database',
            name='shortcode',
            field=models.CharField(default='abc', max_length=20),
            preserve_default=False,
        ),
    ]
