# Generated by Django 4.1.2 on 2023-06-20 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0017_category_image_alter_withdraw_amount'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeamMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('role', models.CharField(max_length=100)),
                ('image', models.ImageField(default='user_photos/img.jpg', upload_to='user_photos')),
            ],
        ),
    ]