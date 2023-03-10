# Generated by Django 4.1.5 on 2023-01-14 11:02

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("properties", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="property",
            name="owner",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="property",
            name="bed_rooms",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="property",
            name="gas",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="property",
            name="internet",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="property",
            name="latitude",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="property",
            name="longitude",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="property",
            name="rooms",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="property",
            name="total_area",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="property",
            name="tv",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="property",
            name="water",
            field=models.BooleanField(default=False),
        ),
    ]
