# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0003_auto_20151204_2214'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('ref_id', models.CharField(max_length=100, null=True, blank=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=200, null=True, blank=True)),
                ('detailed_review', models.CharField(max_length=1000, null=True, blank=True)),
                ('recommended', models.NullBooleanField()),
                ('user', models.ForeignKey(blank=True, to='customers.Users', null=True)),
            ],
            options={
                'db_table': 'reviews',
                'managed': True,
            },
        ),
    ]
