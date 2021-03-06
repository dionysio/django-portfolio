# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-12 20:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artwork',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveIntegerField(db_index=True, default=0, editable=False)),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('description', models.TextField(blank=True, verbose_name='description')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modified')),
            ],
            options={
                'verbose_name': 'work',
                'verbose_name_plural': 'works',
                'abstract': False,
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveIntegerField(db_index=True, default=0, editable=False)),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('slug', models.SlugField(unique=True, verbose_name='slug')),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
                'abstract': False,
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveIntegerField(db_index=True, default=0, editable=False)),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('slug', models.SlugField(unique=True, verbose_name='slug')),
                ('description', models.TextField(blank=True, verbose_name='description')),
            ],
            options={
                'verbose_name': 'collection',
                'verbose_name_plural': 'collections',
                'abstract': False,
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveIntegerField(db_index=True, default=0, editable=False)),
                ('title', models.CharField(blank=True, max_length=255, verbose_name='title')),
                ('image', sorl.thumbnail.fields.ImageField(upload_to='portfolio/pictures')),
                ('artwork', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pictures', to='portfolio.Artwork')),
            ],
            options={
                'verbose_name': 'picture',
                'verbose_name_plural': 'pictures',
                'abstract': False,
                'ordering': ['order'],
            },
        ),
        migrations.AddField(
            model_name='artwork',
            name='categories',
            field=models.ManyToManyField(blank=True, related_name='artworks', to='portfolio.Category'),
        ),
        migrations.AddField(
            model_name='artwork',
            name='collection',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='artworks', to='portfolio.Collection'),
        ),
    ]
