# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-20 07:16
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('proposed_date', models.DateTimeField(blank=True, null=True)),
                ('summary', models.CharField(max_length=148)),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('party_affiliation', models.CharField(choices=[('DEM', 'Democrat'), ('REP', 'Republican'), ('THIRD', 'Third Party'), ('IND', 'Independent')], default='IND', max_length=2)),
            ],
        ),
        migrations.AddField(
            model_name='bill',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='bill',
            name='userDownVotes',
            field=models.ManyToManyField(blank=True, related_name='billDownVotes', to='twocents.User'),
        ),
        migrations.AddField(
            model_name='bill',
            name='userUpVotes',
            field=models.ManyToManyField(blank=True, related_name='billUpVotes', to='twocents.User'),
        ),
    ]
