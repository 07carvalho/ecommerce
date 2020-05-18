from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APITestCase
from products.models import Product
from .models import Cart


class CartDetailAPIViewTestCase(APITestCase):

    cart_detail_url = reverse('cart_detail')
    products = []

    def setUp(self):
        # crate a superuser and a cart
        admin = User.objects.create_superuser('admin', email='admin@ecommerce.com', password='admin123')
        self.cart_admin = Cart.objects.create(owner=admin)

        # crate a regular user and a cart
        user = User.objects.create_user('buyer', email='buyer@gmail.com', password='123456')
        self.cart_user = Cart.objects.create(owner=user)

        # insert products in db
        products = [
            {'title': 'Product 1', 'description': 'Description 1', 'price': 1444.90, 'visible': True},
            {'title': 'Product 2', 'description': 'Description 2', 'price': 544.90, 'visible': True},
            {'title': 'Product 3', 'description': 'Description 3', 'price': 344.90, 'visible': True},
            {'title': 'Product 4', 'description': 'Description 4', 'price': 2444.90, 'visible': True},
            {'title': 'Product 5', 'description': 'Description 5', 'price': 2444.90, 'visible': False},
        ]
        for product in products:
            obj = Product.objects.create(**product)
            self.products.append(obj.id)

    def test_cart_posts_empty(self):
        """Get cart details"""
        self.client.login(username='admin', password='admin123')
        response = self.client.get(self.cart_detail_url)
        self.assertEqual(200, response.status_code)
        self.assertEqual(0, len(response.data['items']))
        self.assertEqual(0, response.data['total'])
