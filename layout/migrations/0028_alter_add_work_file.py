# Generated by Django 4.2.7 on 2024-03-28 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('layout', '0027_remove_form_post_image_url_form_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add_work',
            name='File',
            field=models.FileField(upload_to='media/'),
        ),
    ]
