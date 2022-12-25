"""mydjangoproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from foodapp1.views import index_page
from foodapp1.views import locations_page
from foodapp1.views import delete_location
from foodapp1.views import types_page
from foodapp1.views import delete_type
from foodapp1.views import basket_page
from foodapp1.views import delete_basket_product
from foodapp1.views import products_page
from foodapp1.views import delete_product
from foodapp1.views import delete_all_basket_products
from foodapp1.views import make_basket
from foodapp1.views import purchases_page
from foodapp1.views import delete_purchase
from foodapp1.views import edit_basket_product

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_page),
    path('locations/', locations_page),
    path('delete-location/<location_id>/', delete_location, name="delete-location"),
    path('types/', types_page),
    path('delete-type/<type_id>/', delete_type, name="delete-type"),
    path('basket/', basket_page),
    path('delete-basket-product/<basket_product_id>/', delete_basket_product, name="delete-basket-product"),
    path('delete-all-basket-products/', delete_all_basket_products, name="delete-all-basket-products"),
    path('make-basket/', make_basket, name="make-basket"),
    path('products/', products_page),
    path('delete-product/<product_id>/', delete_product, name="delete-product"),
    path('purchases/',purchases_page),
    path('delete-purchase/<purchase_id>/', delete_purchase, name="delete-purchase"),
    path('edit-basket-products/<basket_product_id>/', edit_basket_product, name="edit-basket-product"),
]
