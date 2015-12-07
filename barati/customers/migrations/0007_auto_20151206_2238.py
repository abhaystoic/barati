# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0006_auto_20151206_2226'),
    ]

    operations = [
        migrations.CreateModel(
            name='Card_Colors',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('ref_id', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=20)),
                ('hexcode', models.CharField(max_length=7)),
            ],
            options={
                'db_table': 'card_colors',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Card_Deities',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('ref_id', models.CharField(max_length=100)),
                ('top_deity_image', models.CharField(max_length=30)),
                ('inside_deity_image', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'card_deities',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='cards',
            name='weight',
            field=models.FloatField(null=True, blank=True),
        ),
    ]
