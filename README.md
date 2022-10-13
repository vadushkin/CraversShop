# Cravers

Anon is a fully responsive e commerce website, 
maximum compatiblities in all mobile devices, 
built using HTML, CSS, and JavaScript.

Original: https://github.com/codewithsadee/anon-ecommerce-website

Demo
----------

![Anon Desktop Demo](website-demo-image/desktop.png "Desktop Demo")
![Anon Mobile Demo](website-demo-image/mobile.png "Mobile Demo")


Installing 
----------

#### Requirements:
* Python >= 3.10
* Django >= 3.0 / 4.0

#### Windows:

```
git clone https://github.com/vadushkin/Cravers_Shop.git
cd Cravers_Shop
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
python.exe -m pip install --upgrade pip
python manage.py runserver
```

#### Admin Panel:
```
python manage.py createsuperuser
```

Installing in Docker
--------------------

```
git clone https://github.com/vadushkin/Cravers_Shop.git
cd Cravers_Shop
docker-compose up -d
```

#### Docker stop:

```
docker-compose stop
```

Services
--------

* `/` - Home Page
* `admin/` - Admin
* `blogs/` - Blogs
* `blog/slug:slug/` - Blog
* `category/slug:slug/` - Category
* `product/slug:slug/` - Product
* `cart/` - Cart
* `checkout/` - Checkout

Api
---

* `products/` - All products
* `products/pk:int/` - Product
* `best_products/` - All the best products
* `best_products/pk:int/` - The best product
* `products_of_the_day/` - The products of the day 
* `products_of_the_day/pk:int/` - The product of the day 
* `blogs/` - All Blogs
* `blogs/pk:int/` - Blog
* `categories/` - All categories
* `categories/pk:int/` - Category
* `popular_categories/` - All Popular Categories
* `popular_categories/pk:int/` - Popular Category
* `customers/` - All customers
* `customers/pk:int/` - Customer