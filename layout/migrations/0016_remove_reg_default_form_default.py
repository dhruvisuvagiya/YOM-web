# Generated by Django 4.2.7 on 2024-03-13 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('layout', '0015_reg_default'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reg',
            name='Default',
        ),
        migrations.AddField(
            model_name='form',
            name='Default',
            field=models.BooleanField(default=0),
        ),
    ]
