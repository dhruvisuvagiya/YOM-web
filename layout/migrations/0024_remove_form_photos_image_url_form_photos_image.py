# Generated by Django 4.2.7 on 2024-03-21 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('layout', '0023_alter_form_default'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='form_photos',
            name='Image_URL',
        ),
        migrations.AddField(
            model_name='form_photos',
            name='Image',
            field=models.FileField(default='nophoto', upload_to='media/'),
        ),
    ]