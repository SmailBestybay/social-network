# Generated by Django 4.0.6 on 2022-07-29 19:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0005_alter_post_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='created_on',
            new_name='timestamp',
        ),
    ]