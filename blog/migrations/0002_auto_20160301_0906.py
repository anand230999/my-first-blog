# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-01 03:36
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 1, 3, 36, 22, 918327, tzinfo=utc)),
        ),
    ]
