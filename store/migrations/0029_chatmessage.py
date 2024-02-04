# Generated by Django 3.2.4 on 2024-02-03 15:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0028_delete_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatMessage',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('text', models.TextField()),
                ('file', models.FileField(blank=True, null=True, upload_to='chat_files/')),
                ('image', models.ImageField(blank=True, null=True, upload_to='chat_images/')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('recipient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='received_messages', to='store.customer')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sent_messages', to='store.customer')),
            ],
        ),
    ]
