# ecommerce
An e-commerce API with Django

#### Stack used:
* Django 2.2.12    
* Django Rest Framework 3.11
* Docker
* PostgreSQL

#### Init
In the root project, run:
> docker-compose build

Then, run:
> docker-compose up

For a better experience, use the Browsable API in
> [localhost:8000/login/](http://localhost:8000/login/)

## API Routes
#### Create User
Create a regular user (buyer). Admin user must be created using Django commands.
| Field | Description |
|--|--|    
| URL | [/api/v1/auth/register/](http://localhost:8000/api/v1/auth/register/) |
| Method | `POST` |
| URL Params | **Required** <br> None <br><br> **Optional** <br> None |
| Data Params | `{"email": [string], "username": [string], "password": [string], "first_name": [string], "last_name": [string]]}` <br><br> **Example** <br> `{"email": "email@email.com", "username": "new_username", "password": "password", "first_name": "Name", "last_name": "Lastname"}` |
| Samples Call | `curl -d {"email": "email@email.com", "username": "new_username", "password": "password", "first_name": "Name", "last_name": "Lastname"} -X POST http://localhost:8000/api/v1/auth/register/` |

#### Login User
Do login.
| Field | Description |
|--|--|    
| URL | [/api/v1/auth/signin/](http://localhost:8000/api/v1/auth/signin/) |
| Method | `POST` |
| URL Params | **Required** <br> None <br><br> **Optional** <br> None |
| Data Params | `{"username": [string], "password": [string]}` <br><br> **Example** <br> `{"username": "new_username", "password": "password"}` |
| Samples Call | `curl -d {"username": "new_username", "password": "password"} -X POST http://localhost:8000/api/v1/auth/signin/` |

#### List Products
List all visible products.
| Field | Description |
|--|--|    
| URL | [/api/v1/products/](http://localhost:8000/api/v1/products/) |
| Method | `GET` |
| URL Params | **Required** <br> None <br><br> **Optional** <br> `search=[string]` |
| Data Params | None |
| Samples Call | `curl --request GET 'http://localhost:8000/api/v1/products/'` |

#### Create a Product
Create a new product  (only for superusers)
| Field | Description  |
|--|--|
| URL | [/api/v1/products/](http://localhost:8000/api/v1/products/1/) |
| Method | `POST` |
| URL Params | **Required** <br> None <br><br> **Optional** <br> None |
| Data Params | `{"title": [string], "description": [string], "price": [float], "visible": [boolean]}` <br><br> **Example** <br> `{"title": "Product 1", "description": "Description 1", "price": 9999.99, "visible": true}` |
| Samples Call | `curl -d '{"title": "Product 1", "description": "Description 1", "price": 9999.99, "visible": true}' -H 'Authorization: Token [string]' -H "Content-Type: application/json" -X POST 'http://localhost:8000/api/v1/products/'` |

#### Get a Product
Get a specific product.
| Field | Description |
|--|--|
| URL | [/api/v1/products/:id/](http://localhost:8000/api/v1/products/1/) |
| Method | `GET` |
| URL Params | **Required** <br> `id=[int]` <br><br> **Optional** <br> None |
| Data Params | None |
| Samples Call | `curl --request GET 'http://localhost:8000/api/v1/products/1/'` |

#### Get User's Cart
Logged User get data from own Cart.
| Field | Description |
|--|--|
| URL | [/api/v1/carts/](http://localhost:8000/api/v1/carts/) |
| Method | `GET` |
| URL Params | **Required** <br> None <br><br> **Optional** <br> None |
| Data Params | None |
| Samples Call | `curl -H 'Authorization: Token [string]' -H "Content-Type: application/json" -X GET 'http://localhost:8000/api/v1/carts/'` |

#### Insert a Product in User's Cart
Logged User insert a Product in own Cart.
| Field | Description |
|--|--|
| URL | [/api/v1/carts/products/](http://localhost:8000/api/v1/carts/products/) |
| Method | `POST` |
| URL Params | **Required** <br> None <br><br> **Optional** <br> None |
| Data Params | `{"quantity": [int], "cart": [int], "product": [int]}` <br><br> **Example** <br> `{"quantity": 1, "cart": 1, "product": 1}` |
| Samples Call | `curl -d '{"quantity": "5", "cart": "2", "product": "3"}' -H 'Authorization: Token [string]' -H "Content-Type: application/json" -X POST 'http://localhost:8000/api/v1/carts/products/'` |

#### Remove all Products from User's Cart
Logged User clear own Cart.
| Field | Description |
|--|--|
| URL | [/api/v1/carts/products/](http://localhost:8000/api/v1/carts/products/) |
| Method | `DELETE` |
| URL Params | **Required** <br> None <br><br> **Optional** <br> None |
| Data Params | None |
| Samples Call | `curl -H 'Authorization: Token [string]' --request DELETE 'http://localhost:8000/api/v1/carts/products/'` |

#### Update a single Product in User's Cart
Logged User update the quantity of a Product in own Cart.
| Field | Description |
|--|--|
| URL | [/api/v1/carts/products/:id/](http://localhost:8000/api/v1/carts/products/1/) |
| Method | `PUT` |
| URL Params | **Required** <br> `id=[int]` <br><br> **Optional** <br> None |
| Data Params | None |
| Samples Call | `curl -d -d '{"quantity": 10} --request PUT 'http://localhost:8000/api/v1/carts/products/1/'` |

#### Remove a single Product from User's Cart
Logged User remove a Product from own Cart.
| Field | Description |
|--|--|
| URL | [/api/v1/carts/products/:id/](http://localhost:8000/api/v1/carts/products/1/) |
| Method | `DELETE` |
| URL Params | **Required** <br> `id=[int]` <br><br> **Optional** <br> None |
| Data Params | None |
| Samples Call | `curl -d --request DELETE 'http://localhost:8000/api/v1/carts/products/1/'` |

#### List User's Order
Logged User list all own orders.
| Field | Description |
|--|--|
| URL | [/api/v1/orders/](http://localhost:8000/api/v1/orders/) |
| Method | `GET` |
| URL Params | **Required** <br> None <br><br> **Optional** <br> None |
| Data Params | None |
| Samples Call | `curl -d --request POST 'http://localhost:8000/api/v1/orders/'` |

#### Make a Order
Logged User make a Order only if has Products in the Cart.
| Field | Description |
|--|--|
| URL | [/api/v1/orders/](http://localhost:8000/api/v1/orders/) |
| Method | `POST` |
| URL Params | **Required** <br> None <br><br> **Optional** <br> None |
| Data Params | `{"address": {"address": [string],  "state": [string], "country": [string], "zip_code": [string]}}` <br><br> **Example** <br> `{"address": {"address": "Street, number, Town",  "state": "State", "country": "Country", "zip_code": "00000-000"}}` |
| Samples Call | `curl -d '{"address": {"address": "Street, number, Town",  "state": "State", "country": "Country", "zip_code": "00000-000"}}' --request POST 'http://localhost:8000/api/v1/orders/'` |

### Tests
Run tests with
> docker-compose run api python manage.py test
