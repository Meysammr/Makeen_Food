# Generated by Django 4.1.4 on 2023-05-10 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_panel', '0027_payment_order_number_alter_payment_transaction_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='order_number',
            field=models.BigIntegerField(default=1000000),
        ),
    ]
