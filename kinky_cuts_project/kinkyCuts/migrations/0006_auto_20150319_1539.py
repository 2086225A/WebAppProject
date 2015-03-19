# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('kinkyCuts', '0005_auto_20150319_1535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creation',
            name='creationDate',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 19, 15, 39, 9, 431000), verbose_name=b'Date Published'),
        ),
    ]
