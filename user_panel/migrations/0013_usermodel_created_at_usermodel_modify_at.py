# Generated by Django 4.1.4 on 2023-04-17 20:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('user_panel', '0012_usermodel_on_delete'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodel',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usermodel',
            name='modify_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
