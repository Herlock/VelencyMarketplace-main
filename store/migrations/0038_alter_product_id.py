# Generated by Django 4.1.2 on 2023-04-08 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0037_alter_product_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]