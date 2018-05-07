# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-05-07 23:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_kaya'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
            ],
        ),
        migrations.AlterField(
            model_name='kaya',
            name='name',
            field=models.CharField(max_length=60),
        ),
    ]
