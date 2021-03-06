# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-01 12:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import weblate.utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('trans', '0122_auto_20180129_1507'),
    ]

    operations = [
        migrations.CreateModel(
            name='Addon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('configuration', weblate.utils.fields.JSONField()),
                ('state', weblate.utils.fields.JSONField()),
                ('component', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trans.SubProject')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.IntegerField(choices=[(1, 'post push'), (2, 'post update'), (3, 'pre commit'), (4, 'post commit')])),
                ('addon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='addons.Addon')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='event',
            unique_together=set([('addon', 'event')]),
        ),
        migrations.AlterUniqueTogether(
            name='addon',
            unique_together=set([('component', 'name')]),
        ),
    ]
