# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0011_auto_20151210_2248'),
    ]

    operations = [
        migrations.AddField(
            model_name='beauticians',
            name='gender',
            field=models.CharField(default='neutral', max_length=10, choices=[(b'male', b'male'), (b'female', b'female'), (b'neutral', b'neutral')]),
            preserve_default=False,
        ),
    ]
