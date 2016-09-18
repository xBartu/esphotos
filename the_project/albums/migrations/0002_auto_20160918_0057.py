# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-18 00:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='org_link',
            field=models.URLField(max_length=300, verbose_name='The Original Url'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='photo',
            field=models.ImageField(upload_to='albums/photos'),
        ),
    ]
