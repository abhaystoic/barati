# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0006_auto_20160201_2347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beauticians',
            name='home_visit_charge',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='product_pictures',
            name='name',
            field=models.CharField(max_length=100, unique=True, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='venues',
            name='generator_cost',
            field=models.FloatField(null=True, blank=True),
        ),
    ]
