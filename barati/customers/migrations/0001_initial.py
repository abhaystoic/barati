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
                ('timestamp', models.DateTimeField(auto_now_add=True, null=True)),
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
            name='Beauticians',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('ref_id', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=10, choices=[(b'male', b'male'), (b'female', b'female'), (b'neutral', b'neutral')])),
                ('short_description', models.CharField(max_length=100, null=True, blank=True)),
                ('long_description', models.CharField(max_length=800, null=True, blank=True)),
                ('services', models.CharField(max_length=800, null=True, blank=True)),
                ('actual_price', models.IntegerField()),
                ('discount_perc', models.FloatField(null=True, blank=True)),
                ('discount_rs', models.FloatField(null=True, blank=True)),
                ('discounted_price', models.FloatField(null=True, blank=True)),
                ('unisex', models.NullBooleanField()),
                ('female_person_available', models.NullBooleanField()),
                ('home_visit_charge', models.IntegerField(null=True, blank=True)),
                ('home_visit_policy', models.CharField(max_length=800, null=True, blank=True)),
                ('barati_confidence_perc', models.FloatField(null=True, blank=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True, null=True)),
                ('type', models.ForeignKey(blank=True, to='customers.Beautician_Types', null=True)),
            ],
            options={
                'db_table': 'beauticians',
                'managed': True,
            },
        ),
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
            ],
            options={
                'db_table': 'budget',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Card_Colors',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('ref_id', models.CharField(max_length=100, null=True, blank=True)),
                ('color', models.CharField(max_length=20, null=True, blank=True)),
                ('hexcode', models.CharField(max_length=7, null=True, blank=True)),
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
                ('ref_id', models.CharField(max_length=100, null=True, blank=True)),
                ('top_deity_image_path', models.CharField(max_length=200, null=True, blank=True)),
                ('top_deity_name', models.CharField(max_length=30, null=True, blank=True)),
                ('inner_deity_image_path', models.CharField(max_length=200, null=True, blank=True)),
                ('inner_deity_name', models.CharField(max_length=30, null=True, blank=True)),
            ],
            options={
                'db_table': 'card_deities',
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
                ('printing_price', models.FloatField(null=True, blank=True)),
                ('discount_perc', models.FloatField(null=True, blank=True)),
                ('discount_rs', models.FloatField(null=True, blank=True)),
                ('discounted_price', models.FloatField(null=True, blank=True)),
                ('length', models.FloatField(null=True, blank=True)),
                ('width', models.FloatField(null=True, blank=True)),
                ('weight', models.FloatField(null=True, blank=True)),
                ('barati_confidence_perc', models.FloatField(null=True, blank=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True, null=True)),
                ('type', models.ForeignKey(blank=True, to='customers.Card_Types', null=True)),
            ],
            options={
                'db_table': 'cards',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Cards_Preferences',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('ref_id', models.CharField(max_length=100)),
                ('avail_printing', models.NullBooleanField()),
                ('card', models.ForeignKey(to='customers.Cards')),
            ],
            options={
                'db_table': 'cards_preferences',
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
            name='Main_Preferences',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('date', models.DateField(null=True, blank=True)),
                ('location', models.CharField(max_length=50, null=True, blank=True)),
                ('sublocation', models.CharField(max_length=50, null=True, blank=True)),
            ],
            options={
                'db_table': 'main_preferences',
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
            name='Orders',
            fields=[
                ('order_id', models.AutoField(serialize=False, primary_key=True)),
                ('ref_id', models.CharField(max_length=100)),
                ('quantity', models.IntegerField(null=True, blank=True)),
                ('total_price', models.FloatField(null=True, blank=True)),
                ('package_id', models.CharField(unique=True, max_length=100)),
                ('vendor_acknowledgement', models.CharField(max_length=51)),
                ('payment_done', models.BooleanField(default=False)),
                ('payment_received', models.BooleanField(default=False)),
                ('payment_method', models.CharField(max_length=100, null=True, blank=True)),
                ('product_type', models.CharField(max_length=100, null=True, blank=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('address', models.ForeignKey(blank=True, to='customers.Address', null=True)),
            ],
            options={
                'db_table': 'orders',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Photo_Video_Types',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'photo_video_types',
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
            name='Reviews',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('ref_id', models.CharField(max_length=100, null=True, blank=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=200, null=True, blank=True)),
                ('detailed_review', models.CharField(max_length=1000, null=True, blank=True)),
                ('recommended', models.CharField(max_length=10, null=True, blank=True)),
            ],
            options={
                'db_table': 'reviews',
                'managed': True,
            },
        ),
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
                ('max_capacity', models.IntegerField()),
                ('accomodation_available', models.NullBooleanField()),
                ('actual_price', models.IntegerField()),
                ('discount_perc', models.FloatField(null=True, blank=True)),
                ('discount_rs', models.FloatField(null=True, blank=True)),
                ('discounted_price', models.FloatField(null=True, blank=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True, null=True)),
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
            model_name='reviews',
            name='user',
            field=models.ForeignKey(blank=True, to='customers.Users', null=True),
        ),
        migrations.AddField(
            model_name='orders',
            name='user',
            field=models.ForeignKey(blank=True, to='customers.Users', null=True),
        ),
        migrations.AddField(
            model_name='main_preferences',
            name='user',
            field=models.ForeignKey(to='customers.Users'),
        ),
        migrations.AddField(
            model_name='delivery_status',
            name='order',
            field=models.ForeignKey(blank=True, to='customers.Orders', null=True),
        ),
        migrations.AddField(
            model_name='cart',
            name='user',
            field=models.ForeignKey(to='customers.Users'),
        ),
        migrations.AddField(
            model_name='cards_preferences',
            name='user',
            field=models.ForeignKey(blank=True, to='customers.Users', null=True),
        ),
        migrations.AddField(
            model_name='cards',
            name='vendor_id',
            field=models.ForeignKey(to='customers.Vendors'),
        ),
        migrations.AddField(
            model_name='card_deities',
            name='card',
            field=models.ForeignKey(blank=True, to='customers.Cards', null=True),
        ),
        migrations.AddField(
            model_name='card_colors',
            name='card',
            field=models.ForeignKey(blank=True, to='customers.Cards', null=True),
        ),
        migrations.AddField(
            model_name='budget',
            name='user',
            field=models.ForeignKey(to='customers.Users'),
        ),
        migrations.AddField(
            model_name='beauticians',
            name='vendor_id',
            field=models.ForeignKey(to='customers.Vendors'),
        ),
    ]
