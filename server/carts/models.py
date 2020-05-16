from django.contrib.auth.models import User
from django.db import models
from products.models import Product


class Cart(models.Model):
    """Cart has an unique instance per user"""
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    item = models.ManyToManyField(Product, through='CartItem', related_name='products')
    created_at = models.DateTimeField(auto_now=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = 'carts'
        db_table = 'api_cart'

    def __str__(self):
        return '{0}´s Cart'.format(self.owner.username)

    def get_total(self):
        """Calculate the total value of products in the cart"""
        total = 0
        for item in self.cartitem_set.all():
            subtotal = item.quantity * item.product.price
            total += subtotal
        return total


class CartItem(models.Model):
    """The products put by an user in a cart"""
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        app_label = 'carts'
        db_table = 'api_cart_item'
        unique_together = [['cart', 'product']]

    def __str__(self):
        return self.product.title
