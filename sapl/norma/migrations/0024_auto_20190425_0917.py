# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-25 12:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('norma', '0023_auto_20190219_1535'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='normarelacionada',
            options={'ordering': ('norma_principal__data', 'norma_relacionada__data'), 'verbose_name': 'Norma Relacionada', 'verbose_name_plural': 'Normas Relacionadas'},
        ),
    ]