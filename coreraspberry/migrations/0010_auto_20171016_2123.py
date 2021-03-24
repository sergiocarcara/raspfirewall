# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-10-17 01:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('coreraspberry', '0009_auto_20171016_2101'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='galeria',
            name='fotos',
        ),
        migrations.AddField(
            model_name='foto',
            name='galeria',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='coreraspberry.Galeria'),
            preserve_default=False,
        ),
    ]
