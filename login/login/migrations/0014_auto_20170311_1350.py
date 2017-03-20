# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-11 13:50
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0013_userloginform_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userloginform',
            name='user',
        ),
        migrations.AlterField(
            model_name='userloginform',
            name='email',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
