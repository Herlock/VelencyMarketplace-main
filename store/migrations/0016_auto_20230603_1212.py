# Generated by Django 4.1.2 on 2023-06-03 08:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0015_withdraw'),
    ]

    operations = [
    migrations.RemoveField(
        model_name='category',
        name='image',
    ),
]
