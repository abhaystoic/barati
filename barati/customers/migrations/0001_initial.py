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
            name='Bakery_Types',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'bakery_types',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Band_Types',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'band_types',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Beautician_Types',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'beautician_types',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Card_Types',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'card_types',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Cards',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('ref_id', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('short_description', models.CharField(max_length=100)),
                ('long_description', models.CharField(max_length=800)),
                ('min_numbers', models.IntegerField()),
                ('max_numbers', models.IntegerField()),
                ('actual_price', models.IntegerField()),
                ('discount_rs', models.FloatField(null=True, blank=True)),
                ('discounted_price', models.FloatField(null=True, blank=True)),
                ('type', models.ForeignKey(blank=True, to='customers.Card_Types', null=True)),
            ],
            options={
                'db_table': 'cards',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('ref_id', models.CharField(max_length=100)),
                ('product_type', models.CharField(max_length=50)),
                ('checked_out', models.BooleanField(default=False)),
                ('quantity', models.IntegerField(null=True, blank=True)),
                ('total_price', models.FloatField(null=True, blank=True)),
            ],
            options={
                'db_table': 'cart',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Delivery_Status',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('ref_id', models.CharField(max_length=100, null=True, blank=True)),
                ('name', models.CharField(max_length=100, null=True, blank=True)),
                ('status', models.CharField(max_length=100, null=True, blank=True)),
                ('link', models.CharField(max_length=200, null=True, blank=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'delivery_status',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Fireworks_Types',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'fireworks_types',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Ghodi_Bagghi_Types',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'ghodi_bagghi_types',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Gift_Types',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'gift_types',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Mehendi_Types',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'mehendi_types',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Music_Types',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'music_types',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Photo_Types',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'photo_types',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Product_Pictures',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=100, null=True, blank=True)),
                ('ref_id', models.CharField(max_length=100, null=True, blank=True)),
                ('picture_path', models.CharField(max_length=200, null=True, blank=True)),
            ],
            options={
                'db_table': 'product_pictures',
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
            name='Tent_Types',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'tent_types',
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
                ('contact1', models.CharField(blank=True, max_length=50, null=True, validators=[django.core.validators.RegexValidator(regex=b'^\\+?1?\\d{9,15}$', message=b"Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")])),
                ('contact2', models.CharField(blank=True, max_length=50, null=True, validators=[django.core.validators.RegexValidator(regex=b'^\\+?1?\\d{9,15}$', message=b"Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")])),
                ('contact3', models.CharField(blank=True, max_length=50, null=True, validators=[django.core.validators.RegexValidator(regex=b'^\\+?1?\\d{9,15}$', message=b"Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")])),
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
                ('contact1', models.CharField(blank=True, max_length=50, null=True, validators=[django.core.validators.RegexValidator(regex=b'^\\+?1?\\d{9,15}$', message=b"Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")])),
                ('contact2', models.CharField(blank=True, max_length=50, null=True, validators=[django.core.validators.RegexValidator(regex=b'^\\+?1?\\d{9,15}$', message=b"Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")])),
                ('contact3', models.CharField(blank=True, max_length=50, null=True, validators=[django.core.validators.RegexValidator(regex=b'^\\+?1?\\d{9,15}$', message=b"Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")])),
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
            name='Video_Types',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'video_types',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Videos',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('ref_id', models.CharField(max_length=100)),
                ('video_name', models.CharField(max_length=50)),
                ('video_link', models.CharField(max_length=100)),
                ('vendor_id', models.ForeignKey(blank=True, to='customers.Vendors', null=True)),
            ],
            options={
                'db_table': 'videos',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('ref_id', models.CharField(max_length=100, null=True, blank=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(blank=True, to='customers.Users', null=True)),
            ],
            options={
                'db_table': 'wishlist',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='vendor_cordinators',
            name='vendor_id',
            field=models.ForeignKey(blank=True, to='customers.Vendors', null=True),
        ),
        migrations.AddField(
            model_name='cart',
            name='user',
            field=models.ForeignKey(to='customers.Users'),
        ),
        migrations.AddField(
            model_name='cards',
            name='vendor_id',
            field=models.ForeignKey(to='customers.Vendors'),
        ),
    ]
