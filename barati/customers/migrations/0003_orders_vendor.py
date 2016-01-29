# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0002_auto_20160114_1430'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='vendor',
            field=models.ForeignKey(blank=True, to='customers.Vendors', null=True),
        ),
    ]
