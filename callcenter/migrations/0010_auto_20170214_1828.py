# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-14 18:28
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('callcenter', '0009_auto_20170214_1728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videocall',
            name='VC_id',
            field=models.CharField(default=uuid.uuid4, editable=False, max_length=10, primary_key=True, serialize=False, unique=True),
        ),
    ]
