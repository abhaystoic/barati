# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0003_orders_vendor'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='role',
            field=models.CharField(default='customer', max_length=10, choices=[(b'customer', b'customer'), (b'vendor', b'vendor'), (b'admin', b'admin')]),
            preserve_default=False,
        ),
    ]
