# Generated by Django 2.2 on 2021-06-28 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_country_zone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='provider',
            field=models.CharField(choices=[('DHL', 'DHL'), ('UPS', 'UPS'), ('TNT', 'TNT')], max_length=3),
        ),
        migrations.AlterField(
            model_name='price',
            name='provider',
            field=models.CharField(choices=[('DHL', 'DHL'), ('UPS', 'UPS'), ('TNT', 'TNT')], max_length=3),
        ),
    ]