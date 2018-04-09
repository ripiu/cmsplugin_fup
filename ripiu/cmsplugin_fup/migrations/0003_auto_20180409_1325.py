# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-09 11:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmsplugin_fup', '0002_auto_20171019_1021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fupitempluginmodel',
            name='height_unit',
            field=models.CharField(choices=[('vh', 'vh'), ('vw', 'vw'), ('px', 'pixel'), ('rem', 'root em'), ('%', '%')], max_length=5, verbose_name='unit'),
        ),
        migrations.AlterField(
            model_name='fupitempluginmodel',
            name='width_unit',
            field=models.CharField(choices=[('vw', 'vw'), ('vh', 'vh'), ('px', 'pixel'), ('rem', 'root em'), ('%', '%')], max_length=5, verbose_name='unit'),
        ),
        migrations.AlterField(
            model_name='fupitemposition',
            name='x_unit',
            field=models.CharField(choices=[('vw', 'vw'), ('vh', 'vh'), ('px', 'pixel'), ('rem', 'root em'), ('%', '%')], max_length=5, verbose_name='unit'),
        ),
        migrations.AlterField(
            model_name='fupitemposition',
            name='y_unit',
            field=models.CharField(choices=[('vh', 'vh'), ('vw', 'vw'), ('px', 'pixel'), ('rem', 'root em'), ('%', '%')], max_length=5, verbose_name='unit'),
        ),
    ]
