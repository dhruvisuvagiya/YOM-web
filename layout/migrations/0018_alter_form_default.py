# Generated by Django 4.2.7 on 2024-03-14 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('layout', '0017_remove_form_url_form_image_alter_form_default'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='Default',
            field=models.BooleanField(default=0),
        ),
    ]
