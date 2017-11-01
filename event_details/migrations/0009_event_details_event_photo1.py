# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('event_details', '0008_auto_20171024_1206'),
    ]

    operations = [
        migrations.AddField(
            model_name='event_details',
            name='event_photo1',
            field=models.FileField(upload_to='', default=datetime.datetime(2017, 10, 29, 16, 1, 41, 285413, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
