# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import customers.models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0002_auto_20160201_1626'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='venues',
            name='wheelchair_accessible_details',
        ),
        migrations.AddField(
            model_name='venues',
            name='wheelchair_accessibility',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='cards',
            name='ref_id',
            field=models.CharField(unique=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='product_pictures',
            name='picture',
            field=models.FileField(null=True, upload_to=customers.models.get_image_path, blank=True),
        ),
    ]
