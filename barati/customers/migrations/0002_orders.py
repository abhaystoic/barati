# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('ref_id', models.CharField(max_length=100)),
                ('quantity', models.IntegerField(null=True, blank=True)),
                ('total_price', models.FloatField(null=True, blank=True)),
                ('package_id', models.CharField(max_length=100)),
                ('vendor_acknowledgement', models.CharField(max_length=51)),
                ('payment_done', models.BooleanField(default=False)),
                ('payment_received', models.BooleanField(default=False)),
                ('payment_method', models.CharField(max_length=100, null=True, blank=True)),
                ('product_type', models.CharField(max_length=100, null=True, blank=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('address', models.ForeignKey(blank=True, to='customers.Address', null=True)),
                ('user', models.ForeignKey(blank=True, to='customers.Users', null=True)),
            ],
            options={
                'db_table': 'orders',
                'managed': True,
            },
        ),
    ]
