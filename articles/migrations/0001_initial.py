# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2017-01-21 16:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name=b'Tytul')),
                ('content', models.TextField(verbose_name=b'Zawartosc')),
                ('published', models.DateTimeField(verbose_name=b'Data publikacji')),
                ('image', models.FileField(upload_to=b'images/', verbose_name=b'Obrazek')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name=b'U\xc5\xbcytkownik')),
                ('content', models.TextField(verbose_name=b'Komentarz')),
                ('published', models.DateTimeField(verbose_name=b'Data publikacji')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.Article')),
            ],
        ),
    ]