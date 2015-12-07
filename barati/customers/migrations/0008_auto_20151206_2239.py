# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0007_auto_20151206_2238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card_colors',
            name='color',
            field=models.CharField(max_length=20, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='card_colors',
            name='hexcode',
            field=models.CharField(max_length=7, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='card_colors',
            name='ref_id',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='card_deities',
            name='inside_deity_image',
            field=models.CharField(max_length=30, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='card_deities',
            name='ref_id',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='card_deities',
            name='top_deity_image',
            field=models.CharField(max_length=30, null=True, blank=True),
        ),
    ]
