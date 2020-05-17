from datetime import datetime
from django.contrib.auth.models import User
from django.db import models, transaction
from django.utils.translation import ugettext_lazy as _
from rest_framework import serializers
from products.models import Product
from carts.models import Cart, CartItem


class Order(models.Model):
    """Order instance"""
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    address = models.ForeignKey('OrderAddress', on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        app_label = 'orders'
        db_table = 'api_order'

    def __str__(self):
        return '{0}´s Order'.format(self.user.username)

    @transaction.atomic
    def make_order(self, user, address):
        """Create an Order based in the Products in Cart's User"""
        cart = Cart.objects.get(owner=user)
        items = cart.cartitem_set.all()
        if len(items) > 0:
            address = OrderAddress.objects.create(user=user, **address)
            order = Order.objects.create(user=user, address=address)
            for item in cart.cartitem_set.all():
                product = item.product
                order_item = OrderItem.objects.create(order=order,
                                                      product=product,
                                                      title=product.title,
                                                      price=product.price,
                                                      quantity=item.quantity)
            cart.cartitem_set.all().delete()
            cart.updated_at = datetime.now()
            cart.save()
            return order
        raise serializers.ValidationError({'empty_cart': _('Cart must have at least one product.')})

    def get_total(self):
        """Calculate the total value of products in the cart"""
        total = 0
        items = OrderItem.objects.filter(order=self)
        for item in items:
            subtotal = item.quantity * item.price
            total += subtotal
        return total


class OrderItem(models.Model):
    """As Product can be updated any time, this instance represents a Product
    in the exactly time Order is created
    """
    order = models.ForeignKey('Order', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=60, blank=False, null=False)
    price = models.DecimalField(max_digits=12, decimal_places=2, default=0, blank=False, null=False)
    quantity = models.PositiveIntegerField(blank=False, null=False)

    class Meta:
        app_label = 'orders'
        db_table = 'api_order_item'

    def __str__(self):
        return '{0}´s Cart'.format(self.order)


class OrderAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    # order = models.ForeignKey('Order', on_delete=models.CASCADE)
    address = models.CharField(max_length=300)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=9)

    class Meta:
        app_label = 'orders'
        db_table = 'api_order_address'

    def get_full_address(self):
        return '{0}, {1}, {2}, CEP {3}'.format(self.address, self.state, self.country, self.zip_code)
