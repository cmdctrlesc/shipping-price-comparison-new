# Generated by Django 2.2 on 2021-07-03 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0009_auto_20210702_2345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='service',
            field=models.CharField(choices=[('DHL express worldwide', 'DHL express worldwide'), ('DHL economy select', 'DHL economy select'), ('UPS express saver', 'UPS express saver'), ('UPS standard', 'UPS standard')], max_length=100),
        ),
        migrations.AlterField(
            model_name='price',
            name='service',
            field=models.CharField(choices=[('DHL express worldwide', 'DHL express worldwide'), ('DHL economy select', 'DHL economy select'), ('UPS express saver', 'UPS express saver'), ('UPS standard', 'UPS standard')], max_length=100),
        ),
        migrations.AlterField(
            model_name='surcharge',
            name='service',
            field=models.CharField(choices=[('DHL express worldwide', 'DHL express worldwide'), ('DHL economy select', 'DHL economy select'), ('UPS express saver', 'UPS express saver'), ('UPS standard', 'UPS standard')], max_length=100),
        ),
    ]
