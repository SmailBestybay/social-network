# Generated by Django 4.0.5 on 2022-06-13 01:23

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_alter_listing_winner_delete_bid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='starting_bid',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]