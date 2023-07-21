# Generated by Django 4.1.2 on 2023-05-05 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_rename_balance_usdt_customer_balance_usdt_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='country',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='zipcode',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
    ]