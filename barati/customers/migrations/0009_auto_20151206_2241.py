# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0008_auto_20151206_2239'),
    ]

    operations = [
        migrations.RenameField(
            model_name='card_deities',
            old_name='inside_deity_image',
            new_name='inner_deity_image',
        ),
    ]
