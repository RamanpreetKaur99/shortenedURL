# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2020-03-26 12:46
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='urls',
            name='length',
            field=models.IntegerField(default=10, validators=[django.core.validators.MinValueValidator(10), django.core.validators.MaxValueValidator(20)]),
            preserve_default=False,
        ),
    ]
