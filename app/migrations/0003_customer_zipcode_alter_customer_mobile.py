# Generated by Django 5.1.4 on 2024-12-08 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='zipcode',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='customer',
            name='mobile',
            field=models.IntegerField(default=0),
        ),
    ]