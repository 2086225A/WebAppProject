# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('kinkyCuts', '0009_auto_20150319_1609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creation',
            name='creationDate',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 19, 16, 17, 37), verbose_name=b'Date Published'),
        ),
        migrations.AlterField(
            model_name='creation',
            name='imageID',
            field=models.CharField(unique=True, max_length=5),
        ),
    ]
