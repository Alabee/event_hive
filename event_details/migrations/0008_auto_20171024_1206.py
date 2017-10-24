# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('event_details', '0007_auto_20171012_1512'),
    ]

    operations = [
        migrations.AddField(
            model_name='event_details',
            name='event_date',
            field=models.DateField(default=datetime.datetime(2017, 10, 24, 9, 6, 42, 686539, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='event_details',
            name='event_description',
            field=models.TextField(),
        ),
    ]
