# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('building_number', models.CharField(max_length=50, null=True, blank=True)),
                ('street', models.CharField(max_length=100, null=True, blank=True)),
                ('locality', models.CharField(max_length=50, null=True, blank=True)),
                ('landmark', models.CharField(max_length=50, null=True, blank=True)),
                ('city', models.CharField(max_length=50, null=True, blank=True)),
                ('state', models.CharField(max_length=50, null=True, blank=True)),
                ('country', models.CharField(max_length=50, null=True, blank=True)),
                ('zipcode', models.CharField(max_length=50, null=True, blank=True)),
            ],
            options={
                'db_table': 'address',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Pictures',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('product_ref_id', models.CharField(max_length=100)),
                ('picture_name', models.CharField(max_length=50)),
                ('picture_path', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'pictures',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Religion',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=50)),
            ],
            options={
                'db_table': 'religion',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('username', models.CharField(unique=True, max_length=50)),
                ('first_name', models.CharField(max_length=50, null=True, blank=True)),
                ('middle_name', models.CharField(max_length=100, null=True, blank=True)),
                ('last_name', models.CharField(max_length=50, null=True, blank=True)),
                ('email', models.EmailField(max_length=100, null=True, blank=True)),
                ('contact1', models.CharField(blank=True, max_length=50, validators=[django.core.validators.RegexValidator(regex=b'^\\+?1?\\d{9,15}$', message=b"Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")])),
                ('contact2', models.CharField(blank=True, max_length=50, validators=[django.core.validators.RegexValidator(regex=b'^\\+?1?\\d{9,15}$', message=b"Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")])),
                ('contact3', models.CharField(blank=True, max_length=50, validators=[django.core.validators.RegexValidator(regex=b'^\\+?1?\\d{9,15}$', message=b"Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")])),
                ('address', models.ForeignKey(blank=True, to='customers.Address', null=True)),
                ('religion', models.ForeignKey(blank=True, to='customers.Religion', null=True)),
            ],
            options={
                'db_table': 'users',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Vendor_Cordinators',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('coordinator_name', models.CharField(unique=True, max_length=100)),
                ('email', models.EmailField(max_length=100, null=True, blank=True)),
                ('contact1', models.CharField(blank=True, max_length=50, validators=[django.core.validators.RegexValidator(regex=b'^\\+?1?\\d{9,15}$', message=b"Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")])),
                ('contact2', models.CharField(blank=True, max_length=50, validators=[django.core.validators.RegexValidator(regex=b'^\\+?1?\\d{9,15}$', message=b"Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")])),
                ('contact3', models.CharField(blank=True, max_length=50, validators=[django.core.validators.RegexValidator(regex=b'^\\+?1?\\d{9,15}$', message=b"Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")])),
            ],
            options={
                'db_table': 'vendor_coordinators',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Vendors',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=100)),
                ('official_email', models.EmailField(max_length=100, null=True, blank=True)),
                ('contact1', models.CharField(blank=True, max_length=50, validators=[django.core.validators.RegexValidator(regex=b'^\\+?1?\\d{9,15}$', message=b"Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")])),
                ('contact2', models.CharField(blank=True, max_length=50, validators=[django.core.validators.RegexValidator(regex=b'^\\+?1?\\d{9,15}$', message=b"Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")])),
                ('contact3', models.CharField(blank=True, max_length=50, validators=[django.core.validators.RegexValidator(regex=b'^\\+?1?\\d{9,15}$', message=b"Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")])),
                ('address', models.ForeignKey(blank=True, to='customers.Address', null=True)),
            ],
            options={
                'db_table': 'vendors',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Venue_Types',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'venue_types',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Venues',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('ref_id', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('short_description', models.CharField(max_length=100)),
                ('long_description', models.CharField(max_length=800)),
                ('min_capacity', models.IntegerField()),
                ('max_capacity', models.IntegerField()),
                ('accomodation_available', models.BooleanField()),
                ('address', models.ForeignKey(blank=True, to='customers.Address', null=True)),
                ('type', models.ForeignKey(blank=True, to='customers.Venue_Types', null=True)),
                ('vendor_id', models.ForeignKey(to='customers.Vendors')),
            ],
            options={
                'db_table': 'venues',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Videos',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('product_ref_id', models.CharField(max_length=100)),
                ('video_name', models.CharField(max_length=50)),
                ('video_link', models.CharField(max_length=100)),
                ('vendor_id', models.ForeignKey(blank=True, to='customers.Vendors', null=True)),
            ],
            options={
                'db_table': 'videos',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='vendor_cordinators',
            name='vendor_id',
            field=models.ForeignKey(blank=True, to='customers.Vendors', null=True),
        ),
        migrations.AddField(
            model_name='pictures',
            name='vendor_id',
            field=models.ForeignKey(blank=True, to='customers.Vendors', null=True),
        ),
    ]
