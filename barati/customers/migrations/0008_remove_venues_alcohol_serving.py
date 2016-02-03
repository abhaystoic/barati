# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0007_auto_20160202_1107'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='venues',
            name='alcohol_serving',
        ),
    ]
