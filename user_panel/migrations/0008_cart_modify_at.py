# Generated by Django 4.1.4 on 2023-04-16 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_panel', '0007_cart_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='modify_at',
            field=models.DateField(auto_now=True, null=True),
        ),
    ]
