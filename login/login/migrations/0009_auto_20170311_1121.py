# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-11 11:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0008_auto_20170311_1035'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userloginform',
            name='user',
        ),
        migrations.RemoveField(
            model_name='userloginform',
            name='username',
        ),
    ]
