# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('kinkyCuts', '0004_auto_20150319_1423'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creation',
            name='creationDate',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 19, 15, 35, 8, 415000), verbose_name=b'Date Published'),
        ),
        migrations.AlterField(
            model_name='creation',
            name='imageID',
            field=models.IntegerField(default=0, unique=True),
        ),
    ]
