# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event_details', '0005_auto_20171012_1054'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event_details',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('event_category', models.CharField(max_length=2, choices=[('ART', 'ART & PHOTOGRAPHY'), ('P&C', 'PARTYING & CLUBBING'), ('C&T', 'CONFERENCES & TALKS'), ('TEC', 'E-WORLD')])),
                ('event_name', models.CharField(max_length=255)),
                ('event_description', models.CharField(max_length=1000)),
                ('event_charges', models.CharField(max_length=255)),
            ],
        ),
        migrations.DeleteModel(
            name='Details',
        ),
    ]
