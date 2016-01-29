# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0009_auto_20160114_1350'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tax_And_Refund_Policies',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('product_type', models.CharField(max_length=100, unique=True, null=True, blank=True)),
                ('total_tax', models.FloatField(null=True, blank=True)),
                ('min_payment_needed_before_confirmation', models.FloatField(null=True, blank=True)),
                ('refund_before_confirmation', models.FloatField(null=True, blank=True)),
                ('refund_within_2_days', models.FloatField(null=True, blank=True)),
                ('refund_between_2_7_days', models.FloatField(null=True, blank=True)),
                ('refund_between_7_15_days', models.FloatField(null=True, blank=True)),
                ('refund_between_15_30_days', models.FloatField(null=True, blank=True)),
                ('refund_after_30_days_or_processing', models.FloatField(null=True, blank=True)),
                ('refund_after_die_preparing', models.FloatField(null=True, blank=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'db_table': 'tax_and_refund_policies',
                'managed': True,
            },
        ),
        migrations.DeleteModel(
            name='Photo_Types',
        ),
        migrations.RemoveField(
            model_name='venues',
            name='min_capacity',
        ),
        migrations.AddField(
            model_name='venues',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
