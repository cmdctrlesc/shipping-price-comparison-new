# Generated by Django 2.2 on 2021-07-02 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0008_auto_20210702_2230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='code',
            field=models.CharField(max_length=100),
        ),
    ]
