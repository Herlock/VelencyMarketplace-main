# Generated by Django 4.0.4 on 2022-05-11 14:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0015_customer_address_customer_city_customer_contry_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='photo',
            new_name='image',
        ),
    ]