# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event_details', '0006_auto_20171012_1357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event_details',
            name='event_category',
            field=models.CharField(max_length=2),
        ),
    ]
