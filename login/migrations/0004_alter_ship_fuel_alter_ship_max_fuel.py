# Generated by Django 4.1 on 2022-09-23 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("login", "0003_ship"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ship",
            name="fuel",
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name="ship",
            name="max_fuel",
            field=models.BigIntegerField(),
        ),
    ]