# Generated by Django 4.2.7 on 2024-03-21 05:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('layout', '0025_alter_form_photos_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='form_offer',
            name='Title',
        ),
        migrations.RemoveField(
            model_name='form_photos',
            name='Title',
        ),
    ]
