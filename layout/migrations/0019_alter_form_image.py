# Generated by Django 4.2.7 on 2024-03-15 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('layout', '0018_alter_form_default'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='image',
            field=models.FileField(default=1, upload_to='media/'),
            preserve_default=False,
        ),
    ]
