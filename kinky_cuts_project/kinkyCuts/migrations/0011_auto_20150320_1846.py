# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('kinkyCuts', '0010_auto_20150319_1617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creation',
            name='creationDate',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 20, 18, 46, 14, 354000), verbose_name=b'Date Published'),
        ),
        migrations.AlterField(
            model_name='creation',
            name='picture',
            field=models.ImageField(upload_to=b'media', blank=True),
        ),
    ]
