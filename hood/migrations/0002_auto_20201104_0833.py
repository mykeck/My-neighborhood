# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-11-04 05:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hood', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='user_id',
            new_name='username',
        ),
    ]
