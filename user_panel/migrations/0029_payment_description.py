# Generated by Django 4.1.4 on 2023-05-10 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_panel', '0028_alter_payment_order_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
