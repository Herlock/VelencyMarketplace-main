# Generated by Django 4.1.2 on 2023-06-20 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0019_newsfeed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsfeed',
            name='news_link',
            field=models.URLField(blank=True, null=True),
        ),
    ]