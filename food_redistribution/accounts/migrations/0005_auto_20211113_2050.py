# Generated by Django 3.2.7 on 2021-11-14 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0004_auto_20211113_2022"),
    ]

    operations = [
        migrations.AlterField(
            model_name="foodredistributor",
            name="about",
            field=models.TextField(default="Add a description here!", max_length=500),
        ),
        migrations.AlterField(
            model_name="restaurant",
            name="about",
            field=models.TextField(default="Add a description here!", max_length=500),
        ),
    ]
