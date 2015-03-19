# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kinkyCuts', '0002_auto_20150319_1356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creation',
            name='picture',
            field=models.ImageField(upload_to=b'images', blank=True),
        ),
    ]
