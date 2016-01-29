# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0005_vendors_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='type',
            field=models.CharField(default='vendor', max_length=10, choices=[(b'delivery', b'delivery'), (b'vendor', b'vendor'), (b'customer', b'customer')]),
            preserve_default=False,
        ),
    ]
