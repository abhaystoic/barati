# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0006_address_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='comment',
            field=models.CharField(max_length=500, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='orders',
            name='last_status_time',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
