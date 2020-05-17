from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APITestCase
from products.models import Product
from orders.models import Cart, CartItem


class OrderListAPIViewTestCase(APITestCase):

    cart_url = reverse('cart_detail')
    order_url = reverse('order_list')
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
            {'title': 'Product 1', 'description': 'Description 1', 'price': 1.00, 'visible': True},
            {'title': 'Product 2', 'description': 'Description 2', 'price': 2.00, 'visible': True},
            {'title': 'Product 3', 'description': 'Description 3', 'price': 3.00, 'visible': True},
            {'title': 'Product 4', 'description': 'Description 4', 'price': 4.00, 'visible': True},
            {'title': 'Product 5', 'description': 'Description 5', 'price': 5.00, 'visible': True},
        ]
        for product in products:
            obj = Product.objects.create(**product)
            # insert product in admin cart
            cart_item = CartItem(cart=self.cart_admin, product=obj, quantity=1)
            cart_item.save()
            self.products.append(obj.id)

    def test_order_cart_with_products(self):
        """Do a order using a cart with products"""
        self.client.login(username='admin', password='admin123')
        data = {'address': {
                'address': 'Street, number, Town',
                'state': 'State',
                'country': 'Country',
                'zip_code': '00000-000'
            }
        }
        response = self.client.post(self.order_url, data, format='json')
        self.assertEqual(201, response.status_code)
        self.assertEqual(5, len(response.data['items']))
        self.assertEqual(15.0, response.data['total'])

        # cart should be empty after the order
        response = self.client.get(self.cart_url)
        self.assertEqual(200, response.status_code)
        self.assertEqual(0, len(response.data['items']))
        self.assertEqual(0, response.data['total'])

    def test_order_cart_without_products(self):
        """Do a Order with empty Cart"""
        self.client.login(username='admin', password='admin123')
        data = {'address': {
                'address': 'Street 2, num, Town',
                'state': 'State',
                'country': 'Country',
                'zip_code': '1111-111'
            }
        }
        response = self.client.post(self.cart_url, data, format='json')
        self.assertEqual(405, response.status_code)
