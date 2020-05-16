from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APITestCase
from models import Product


class ProductListAPIViewTestCase(APITestCase):

    url = reverse('product_list')

    def setUp(self):
        # crate a superuser
        User.objects.create_superuser('admin', email='admin@ecommerce.com', password='admin123')

        # crate a regular user
        User.objects.create_user('buyer', email='buyer@gmail.com', password='123456')

        # insert products in db
        products = [
            {'title': 'Product 1', 'description': 'Description 1', 'price': 1444.90},
            {'title': 'Product 2', 'description': 'Description 2', 'price': 544.90},
            {'title': 'Product 3', 'description': 'Description 3', 'price': 344.90},
            {'title': 'Product 4', 'description': 'Description 4', 'price': 2444.90},
        ]
        for product in products:
            Product.objects.create(**product)

    def test_list_posts(self):
        """List the products"""
        response = self.client.get(self.url)
        self.assertEqual(200, response.status_code)
        self.assertEqual(4, len(response.data))

    def test_product_creation_by_superuser(self):
        """Create a new product with superuser credentials"""
        self.client.login(username='admin', password='admin123')
        data = {'title': 'Product 5', 'description': 'Description 5', 'price': 3444.90}
        response = self.client.post(self.url, data)
        self.assertEqual(201, response.status_code)

    def test_product_creation_by_regular_user(self):
        """Forbidden to create a new product without superuser credentials"""
        self.client.login(username='buyer', password='123456')
        data = {'title': 'Product 6', 'description': 'Description 6', 'price': 34.90}
        response = self.client.post(self.url, data)
        self.assertEqual(403, response.status_code)

    def test_product_creation_with_existing_title(self):
        """Forbidden to create a new product without superuser credentials"""
        self.client.login(username='admin', password='admin123')
        data = {'title': 'Product 1', 'description': 'Description 1', 'price': 34.90}
        response = self.client.post(self.url, data)
        self.assertEqual(400, response.status_code)
