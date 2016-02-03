# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0004_auto_20160201_2314'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cards',
            old_name='vendor_id',
            new_name='vendor',
        ),
    ]
