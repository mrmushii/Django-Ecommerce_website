# Generated by Django 5.1.4 on 2024-12-08 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_customer_zipcode_alter_customer_mobile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='mobile',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='customer',
            name='zipcode',
            field=models.IntegerField(),
        ),
    ]
