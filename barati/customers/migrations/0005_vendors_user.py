# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0004_users_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendors',
            name='user',
            field=models.ForeignKey(default=1, to='customers.Users'),
            preserve_default=False,
        ),
    ]
