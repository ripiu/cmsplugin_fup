# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-09 14:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmsplugin_fup', '0003_auto_20180409_1325'),
    ]

    operations = [
        migrations.AddField(
            model_name='fupitempluginmodel',
            name='max_height',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='maximum height'),
        ),
        migrations.AddField(
            model_name='fupitempluginmodel',
            name='max_height_unit',
            field=models.CharField(choices=[('px', 'pixel'), ('rem', 'root em'), ('%', '%'), ('vw', 'vw'), ('vh', 'vh')], default='px', max_length=5, verbose_name='unit'),
        ),
        migrations.AddField(
            model_name='fupitempluginmodel',
            name='max_width',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='maximum width'),
        ),
        migrations.AddField(
            model_name='fupitempluginmodel',
            name='max_width_unit',
            field=models.CharField(choices=[('px', 'pixel'), ('rem', 'root em'), ('%', '%'), ('vw', 'vw'), ('vh', 'vh')], default='px', max_length=5, verbose_name='unit'),
        ),
        migrations.AlterField(
            model_name='fupitempluginmodel',
            name='height_unit',
            field=models.CharField(choices=[('px', 'pixel'), ('rem', 'root em'), ('%', '%'), ('vw', 'vw'), ('vh', 'vh')], default='px', max_length=5, verbose_name='unit'),
        ),
        migrations.AlterField(
            model_name='fupitempluginmodel',
            name='width_unit',
            field=models.CharField(choices=[('px', 'pixel'), ('rem', 'root em'), ('%', '%'), ('vw', 'vw'), ('vh', 'vh')], default='px', max_length=5, verbose_name='unit'),
        ),
        migrations.AlterField(
            model_name='fupitemposition',
            name='x_unit',
            field=models.CharField(choices=[('px', 'pixel'), ('rem', 'root em'), ('%', '%'), ('vw', 'vw'), ('vh', 'vh')], max_length=5, verbose_name='unit'),
        ),
        migrations.AlterField(
            model_name='fupitemposition',
            name='y_unit',
            field=models.CharField(choices=[('px', 'pixel'), ('rem', 'root em'), ('%', '%'), ('vw', 'vw'), ('vh', 'vh')], max_length=5, verbose_name='unit'),
        ),
    ]
