
# ecommerce  
An e-commerce API with Django  
  
#### Stack used:  
* Django 2.2.12  
* Django Rest Framework 3.11  
* Docker  
* ProductgreSQL  

#### Init
In the root project, run:
`docker-compose build`
Then, run:
`docker-compose up`
  
## API Routes  
#### List Products  
List all products.  
| Field | Description  |  
|--|--|  
| URL | [/api/v1/products/](http://localhost:8000/api/v1/products/) |  
| Method | `GET` |  
| URL Params | **Required** <br> None <br><br> **Optional** <br> None |  
| Data Params | None |  
| Samples Call | `curl --request GET 'http://localhost:8000/api/v1/products/'` |  
  
#### Get a Product  
Get a specific product.  
| Field | Description  |  
|--|--|  
| URL | [/api/v1/products/:id/](http://localhost:8000/api/v1/products/1/) |  
| Method | `GET` |  
| URL Params | **Required** <br> `id=[int]` <br><br> **Optional** <br> None |  
| Data Params | None |  
| Samples Call | `curl --request GET 'http://localhost:8000/api/v1/products/1/'` |  
  
#### Create a Product  
Create a new product  (only for superusers)
| Field | Description  |  
|--|--|  
| URL | [/api/v1/products/](http://localhost:8000/api/v1/products/1/) |  
| Method | `POST` |  
| URL Params | **Required** <br> None <br><br> **Optional** <br> None |  
| Data Params | `{"title": [string], "description": [string], "price": [float]}` <br><br> **Example** <br> `{"title": "Product 1", "description": "Description 1", "price": 9999.99}` |  
| Samples Call | `curl -d '{"title": "Product 1", "description": "Description 1", "price": 9999.99}' --request POST 'http://localhost:8000/api/v1/products/'` |