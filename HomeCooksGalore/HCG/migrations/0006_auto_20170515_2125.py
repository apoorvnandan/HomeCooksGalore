# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-15 15:55
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('HCG', '0005_auto_20170515_1849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='dishPublisher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
