# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0008_remove_venues_alcohol_serving'),
    ]

    operations = [
        migrations.AddField(
            model_name='venues',
            name='alcohol_serving',
            field=models.NullBooleanField(),
        ),
    ]
