# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('kinkyCuts', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Ratings',
            new_name='Rating',
        ),
        migrations.RenameField(
            model_name='creation',
            old_name='favourites',
            new_name='picture',
        ),
        migrations.RenameField(
            model_name='rating',
            old_name='Creation',
            new_name='imageID',
        ),
        migrations.AddField(
            model_name='creation',
            name='creationDate',
            field=models.DateTimeField(default=datetime.date(2015, 3, 19), verbose_name=b'Date Published'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='creation',
            name='likes',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='creation',
            name='imageID',
            field=models.CharField(unique=True, max_length=5),
        ),
    ]
