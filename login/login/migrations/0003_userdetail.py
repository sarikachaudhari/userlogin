# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-09 14:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_userloginform_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_d', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.UserLoginForm')),
            ],
        ),
    ]