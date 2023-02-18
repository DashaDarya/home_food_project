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
from foodapp1.views import return_to_basket
from foodapp1.views import edit_purchase
from foodapp1.views import return_to_purchases
from foodapp1.views import add_purchases_from_basket
from foodapp1.views import show_expired
from foodapp1.views import show_old
from foodapp1.views import return_to_locations_page
from foodapp1.views import return_to_types_page
from foodapp1.views import return_to_products_page


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
    path('edit-basket-product/<basket_product_id>/', edit_basket_product, name="edit-basket-product"),
    path('return-to-basket/', return_to_basket, name="return-to-basket"),
    path('edit-purchase/<purchase_id>/', edit_purchase, name="edit-purchase"),
    path('return-to-purchases/', return_to_purchases, name="return-to-purchases"),
    path('add-purchases-from-basket/', add_purchases_from_basket, name="add-purchases-from-basket"),
    path('show-expired/', show_expired, name="show-expired"),
    path('show-old/', show_old, name="show_old"),
    path('return-to-locations', return_to_locations_page, name="return-to-locations"),
    path('return-to-types', return_to_types_page, name='return-to-types'),
    path('return-to-products', return_to_products_page, name='return-to-products')
]
