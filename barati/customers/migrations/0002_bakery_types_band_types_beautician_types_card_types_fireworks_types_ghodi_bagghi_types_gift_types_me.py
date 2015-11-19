# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
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
    ]
