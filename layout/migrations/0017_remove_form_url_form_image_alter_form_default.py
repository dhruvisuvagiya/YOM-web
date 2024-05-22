# Generated by Django 4.2.7 on 2024-03-14 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('layout', '0016_remove_reg_default_form_default'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='form',
            name='URL',
        ),
        migrations.AddField(
            model_name='form',
            name='image',
            field=models.FileField(null=True, upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='form',
            name='Default',
            field=models.BooleanField(default=0, null=True),
        ),
    ]
