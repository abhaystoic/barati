# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0008_auto_20160105_0012'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Video_Types',
            new_name='Photo_Video_Types',
        ),
        migrations.AddField(
            model_name='venues',
            name='alcohol_serving',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='venues',
            name='audio_video_equipment_details',
            field=models.CharField(max_length=800, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='venues',
            name='cutlery_and_crockery_details',
            field=models.CharField(max_length=800, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='venues',
            name='food_type',
            field=models.CharField(max_length=800, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='venues',
            name='function_types',
            field=models.CharField(max_length=800, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='venues',
            name='generator_details',
            field=models.CharField(max_length=800, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='venues',
            name='guest_rooms_details',
            field=models.CharField(max_length=800, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='venues',
            name='kitchen_equipment_details',
            field=models.CharField(max_length=800, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='venues',
            name='number_of_rooms',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='venues',
            name='other_services',
            field=models.CharField(max_length=800, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='venues',
            name='outside_catering_allowed',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='venues',
            name='outside_decoration_allowed',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='venues',
            name='parking_capacity',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='venues',
            name='per_plate_cost_nonveg',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='venues',
            name='per_plate_cost_veg',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='venues',
            name='per_room_per_day_cost',
            field=models.FloatField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='venues',
            name='service_staff_details',
            field=models.CharField(max_length=800, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='venues',
            name='stage_details',
            field=models.CharField(max_length=800, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='venues',
            name='valet_parking',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='venues',
            name='wheelchair_accessible_details',
            field=models.CharField(max_length=800, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='venues',
            name='accomodation_available',
            field=models.NullBooleanField(),
        ),
        migrations.AlterModelTable(
            name='photo_video_types',
            table='photo_video_types',
        ),
    ]
