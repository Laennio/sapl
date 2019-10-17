# -*- coding: utf-8 -*-
# Generated by Django 1.11.25 on 2019-10-17 14:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('parlamentares', '0035_merge_20190802_0954'),
    ]

    operations = [
        migrations.CreateModel(
            name='ParlamentarFrente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_entrada', models.DateField(verbose_name='Data Entrada')),
                ('data_saida', models.DateField(blank=True, null=True, verbose_name='Data Saída')),
                ('frente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parlamentares.Frente', verbose_name='Frente')),
                ('parlamentar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parlamentares.Parlamentar', verbose_name='Parlamentar')),
            ],
            options={
                'verbose_name': 'Parlamentar',
                'verbose_name_plural': 'Parlamentares',
            },
        ),
    ]
