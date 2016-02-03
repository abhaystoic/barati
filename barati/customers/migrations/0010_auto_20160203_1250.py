# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0009_venues_alcohol_serving'),
    ]

    operations = [
        migrations.RenameField(
            model_name='beauticians',
            old_name='vendor_id',
            new_name='vendor',
        ),
        migrations.AlterField(
            model_name='beauticians',
            name='ref_id',
            field=models.CharField(unique=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='venues',
            name='ref_id',
            field=models.CharField(unique=True, max_length=100),
        ),
    ]
