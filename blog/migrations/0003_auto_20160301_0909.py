# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-01 03:39
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20160301_0906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2016, 3, 1, 3, 39, 30, 684420, tzinfo=utc)),
        ),
    ]
