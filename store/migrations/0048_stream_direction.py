# Generated by Django 4.1.2 on 2023-12-22 22:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0047_remove_stream_customers_remove_stream_direction_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='stream',
            name='direction',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='store.direction'),
        ),
    ]
