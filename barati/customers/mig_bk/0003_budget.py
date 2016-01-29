# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0002_address_timestamp'),
    ]

    operations = [
        migrations.CreateModel(
            name='Budget',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('min_master', models.FloatField(null=True, blank=True)),
                ('max_master', models.FloatField(null=True, blank=True)),
                ('min_venue', models.FloatField(null=True, blank=True)),
                ('max_venue', models.FloatField(null=True, blank=True)),
                ('min_card', models.FloatField(null=True, blank=True)),
                ('max_card', models.FloatField(null=True, blank=True)),
                ('min_beautician', models.FloatField(null=True, blank=True)),
                ('max_beautician', models.FloatField(null=True, blank=True)),
                ('min_mehendi', models.FloatField(null=True, blank=True)),
                ('max_mehendi', models.FloatField(null=True, blank=True)),
                ('min_music', models.FloatField(null=True, blank=True)),
                ('max_music', models.FloatField(null=True, blank=True)),
                ('min_gift', models.FloatField(null=True, blank=True)),
                ('max_gift', models.FloatField(null=True, blank=True)),
                ('min_tent', models.FloatField(null=True, blank=True)),
                ('max_tent', models.FloatField(null=True, blank=True)),
                ('user', models.ForeignKey(to='customers.Users')),
            ],
            options={
                'db_table': 'budget',
                'managed': True,
            },
        ),
    ]
