# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2019-02-04 11:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0113_auto_20190204_1221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='members.Department'),
        ),
        migrations.AlterField(
            model_name='department',
            name='name',
            field=models.CharField(help_text='Vi tilføjer automatisk "Coding Pirates" foran navnet når vi nævner det de fleste steder på siden.', max_length=200, verbose_name='Navn'),
        ),
    ]
