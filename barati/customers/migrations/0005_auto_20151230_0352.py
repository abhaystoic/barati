# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0004_main_preferences'),
    ]

    operations = [
        migrations.AlterField(
            model_name='main_preferences',
            name='location',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='main_preferences',
            name='sublocation',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
    ]
