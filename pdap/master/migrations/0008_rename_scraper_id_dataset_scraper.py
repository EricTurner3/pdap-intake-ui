# Generated by Django 3.2 on 2021-05-01 17:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0007_auto_20210501_1320'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dataset',
            old_name='scraper_id',
            new_name='scraper',
        ),
    ]