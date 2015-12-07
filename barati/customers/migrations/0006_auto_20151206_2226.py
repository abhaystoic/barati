# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0005_auto_20151206_2159'),
    ]

    operations = [
        migrations.AddField(
            model_name='cards',
            name='length',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='cards',
            name='width',
            field=models.FloatField(null=True, blank=True),
        ),
    ]
