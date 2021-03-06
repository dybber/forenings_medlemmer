# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2019-02-04 19:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0114_auto_20190204_1223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='door',
            field=models.CharField(blank=True, default='', max_length=5, verbose_name='Dør'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='person',
            name='floor',
            field=models.CharField(blank=True, default='', max_length=3, verbose_name='Etage'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='person',
            name='placename',
            field=models.CharField(blank=True, default='', max_length=200, verbose_name='Stednavn'),
            preserve_default=False,
        ),
    ]
