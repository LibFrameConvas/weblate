# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-03-20 14:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trans', '0127_auto_20180320_1547'),
    ]

    operations = [
        migrations.AddField(
            model_name='componentlist',
            name='show_dashboard',
            field=models.BooleanField(db_index=True, default=True, help_text='When enabled this component list will be shown as a tab on the dashboard', verbose_name='Show on dashboard'),
        ),
    ]
