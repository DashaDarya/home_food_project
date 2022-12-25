from django.contrib import admin
from foodapp1.models import Location
from foodapp1.models import Type
from foodapp1.models import Product
from foodapp1.models import Purchase
from foodapp1.models import Basket


admin.site.register(Location)
admin.site.register(Type)
admin.site.register(Product)
admin.site.register(Purchase)
admin.site.register(Basket)
