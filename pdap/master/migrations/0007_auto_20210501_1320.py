# Generated by Django 3.2 on 2021-05-01 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0006_county_population'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data_type',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='format_type',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='scraper',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='source_type',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='update_frequency',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
