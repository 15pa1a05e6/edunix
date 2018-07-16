# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-02 07:50
from __future__ import unicode_literals

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='mobile',
        ),
        migrations.AddField(
            model_name='user',
            name='date_or_birth',
            field=models.DateField(blank=True, null=True, verbose_name='date of birth'),
        ),
        migrations.AddField(
            model_name='user',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, help_text='In case we need to call you', max_length=128, verbose_name='Phone number'),
        ),
        migrations.AddField(
            model_name='user',
            name='title',
            field=models.CharField(blank=True, choices=[('Mr', 'Mr'), ('Miss', 'Miss'), ('Mrs', 'Mrs'), ('Ms', 'Ms'), ('Dr', 'Dr')], max_length=64, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=255, verbose_name='First name'),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(blank=True, max_length=255, verbose_name='Last name'),
        ),
    ]
