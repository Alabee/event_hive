# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event_details', '0009_event_details_event_photo1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event_details',
            name='event_photo1',
        ),
    ]
