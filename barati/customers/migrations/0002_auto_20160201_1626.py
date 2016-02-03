# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='beauticians',
            name='unisex',
        ),
        migrations.AddField(
            model_name='product_pictures',
            name='picture',
            field=models.FileField(null=True, upload_to=b'picture', blank=True),
        ),
    ]
