# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-16 02:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product_app', '0002_product_test_field'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='test_field',
        ),
    ]
