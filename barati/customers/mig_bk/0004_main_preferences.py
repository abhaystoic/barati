# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0003_budget'),
    ]

    operations = [
        migrations.CreateModel(
            name='Main_Preferences',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('date', models.DateField(null=True, blank=True)),
                ('location', models.CharField(unique=True, max_length=50)),
                ('sublocation', models.CharField(unique=True, max_length=50)),
                ('user', models.ForeignKey(to='customers.Users')),
            ],
            options={
                'db_table': 'main_preferences',
                'managed': True,
            },
        ),
    ]
