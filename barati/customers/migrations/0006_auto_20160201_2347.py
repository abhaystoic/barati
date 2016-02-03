# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0005_auto_20160201_2319'),
    ]

    operations = [
        migrations.AddField(
            model_name='beauticians',
            name='address',
            field=models.ForeignKey(blank=True, to='customers.Address', null=True),
        ),
        migrations.AddField(
            model_name='cards',
            name='address',
            field=models.ForeignKey(blank=True, to='customers.Address', null=True),
        ),
        migrations.AlterField(
            model_name='beauticians',
            name='actual_price',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='cards',
            name='actual_price',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='venues',
            name='actual_price',
            field=models.FloatField(),
        ),
    ]
