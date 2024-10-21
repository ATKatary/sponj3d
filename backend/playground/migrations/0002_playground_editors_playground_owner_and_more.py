# Generated by Django 5.1.2 on 2024-10-21 03:16

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playground', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='playground',
            name='editors',
            field=models.ManyToManyField(blank=True, related_name='%(class)s_editors', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='playground',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_owner', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='playground',
            name='viewers',
            field=models.ManyToManyField(blank=True, related_name='%(class)s_viewers', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='playground',
            name='title',
            field=models.CharField(max_length=26),
        ),
    ]
