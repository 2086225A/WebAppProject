# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('kinkyCuts', '0003_auto_20150319_1401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creation',
            name='creationDate',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 19, 14, 23, 35, 98000), verbose_name=b'Date Published'),
        ),
    ]
