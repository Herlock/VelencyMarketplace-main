# Generated by Django 4.1.2 on 2023-03-31 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0019_rename_customer_support_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='id',
            field=models.AutoField(default=None, primary_key=True, serialize=False),
        ),
    ]
