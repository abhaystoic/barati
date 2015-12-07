# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0009_auto_20151206_2241'),
    ]

    operations = [
        migrations.AddField(
            model_name='card_colors',
            name='card',
            field=models.ForeignKey(blank=True, to='customers.Cards', null=True),
        ),
        migrations.AddField(
            model_name='card_deities',
            name='card',
            field=models.ForeignKey(blank=True, to='customers.Cards', null=True),
        ),
    ]
