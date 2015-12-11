# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0010_auto_20151206_2246'),
    ]

    operations = [
        migrations.CreateModel(
            name='Beauticians',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('ref_id', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('short_description', models.CharField(max_length=100, null=True, blank=True)),
                ('long_description', models.CharField(max_length=800, null=True, blank=True)),
                ('services', models.CharField(max_length=800, null=True, blank=True)),
                ('actual_price', models.IntegerField()),
                ('discount_rs', models.FloatField(null=True, blank=True)),
                ('discounted_price', models.FloatField(null=True, blank=True)),
                ('unisex', models.NullBooleanField()),
                ('female_person_available', models.NullBooleanField()),
                ('home_visit_charge', models.IntegerField(null=True, blank=True)),
                ('type', models.ForeignKey(blank=True, to='customers.Beautician_Types', null=True)),
                ('vendor_id', models.ForeignKey(to='customers.Vendors')),
            ],
            options={
                'db_table': 'beauticians',
                'managed': True,
            },
        ),
        migrations.RenameField(
            model_name='card_deities',
            old_name='inner_deity_image',
            new_name='inner_deity_name',
        ),
        migrations.RenameField(
            model_name='card_deities',
            old_name='top_deity_image',
            new_name='top_deity_name',
        ),
        migrations.AddField(
            model_name='card_deities',
            name='inner_deity_image_path',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='card_deities',
            name='top_deity_image_path',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
    ]
