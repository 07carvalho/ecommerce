# Generated by Django 2.2.12 on 2020-05-16 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='item',
            field=models.ManyToManyField(related_name='products', through='carts.CartItem', to='products.Product'),
        ),
    ]
