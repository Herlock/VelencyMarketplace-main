# Generated by Django 4.1.2 on 2023-11-15 12:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0027_course_category_course_description_direction'),
    ]

    operations = [
        migrations.RenameField(
            model_name='direction',
            old_name='description2',
            new_name='hard_skills',
        ),
        migrations.RenameField(
            model_name='direction',
            old_name='description3',
            new_name='soft_skills',
        ),
    ]
