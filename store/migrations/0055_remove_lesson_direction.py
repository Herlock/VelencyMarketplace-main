# Generated by Django 4.1.2 on 2023-12-23 00:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0054_remove_customer_directions_remove_direction_lessons_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lesson',
            name='direction',
        ),
    ]
