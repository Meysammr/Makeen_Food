# Generated by Django 4.1.4 on 2023-05-08 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_panel', '0021_payment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='package',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='rank',
            field=models.CharField(max_length=50, null=True),
        ),
    ]