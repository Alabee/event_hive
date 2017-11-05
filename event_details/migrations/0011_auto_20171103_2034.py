# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('event_details', '0010_remove_event_details_event_photo1'),
    ]

    operations = [
        migrations.AddField(
            model_name='event_details',
            name='event_image',
            field=models.FileField(upload_to='', default=datetime.datetime(2017, 11, 3, 17, 34, 37, 898151, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='event_details',
            name='event_category',
            field=models.CharField(max_length=3),
        ),
    ]
