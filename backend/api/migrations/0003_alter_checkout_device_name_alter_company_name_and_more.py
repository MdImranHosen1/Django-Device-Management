# Generated by Django 5.0 on 2024-01-28 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_remove_checkout_device_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkout',
            name='device_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='company',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='contact_information',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='employee',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]