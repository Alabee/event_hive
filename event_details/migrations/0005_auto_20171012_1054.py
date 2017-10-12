# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event_details', '0004_auto_20170704_1526'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='details',
            name='event_amount',
        ),
        migrations.RemoveField(
            model_name='details',
            name='event_category',
        ),
        migrations.RemoveField(
            model_name='details',
            name='event_date',
        ),
        migrations.RemoveField(
            model_name='details',
            name='event_description',
        ),
        migrations.RemoveField(
            model_name='details',
            name='event_image1',
        ),
        migrations.RemoveField(
            model_name='details',
            name='event_image2',
        ),
        migrations.RemoveField(
            model_name='details',
            name='event_image3',
        ),
        migrations.RemoveField(
            model_name='details',
            name='event_location',
        ),
        migrations.AlterField(
            model_name='details',
            name='event_name',
            field=models.CharField(max_length=255),
        ),
    ]
