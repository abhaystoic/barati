# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0002_orders'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orders',
            old_name='id',
            new_name='order_id',
        ),
        migrations.AddField(
            model_name='delivery_status',
            name='order',
            field=models.ForeignKey(blank=True, to='customers.Orders', null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='package_id',
            field=models.CharField(unique=True, max_length=100),
        ),
    ]
