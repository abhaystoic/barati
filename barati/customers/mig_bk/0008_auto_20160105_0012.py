# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0007_beauticians_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='beauticians',
            name='discount_perc',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='cards',
            name='discount_perc',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='venues',
            name='actual_price',
            field=models.IntegerField(default=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='venues',
            name='discount_perc',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='venues',
            name='discount_rs',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='venues',
            name='discounted_price',
            field=models.FloatField(null=True, blank=True),
        ),
    ]
