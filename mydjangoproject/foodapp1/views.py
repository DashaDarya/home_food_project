from django.shortcuts import render
from django.shortcuts import redirect
from foodapp1.models import Location
from foodapp1.models import Type
from foodapp1.models import Basket
from foodapp1.models import Product
from foodapp1.models import Purchase
from django.http.request import HttpRequest

def index_page(request):
    return render(request, 'index.html')

def locations_page(request: HttpRequest):
    # print(request.GET['product_name'])
    if request.method == "POST":
        loc_name = request.POST['location_name']
        print(loc_name)
        try:
            Location.objects.create(name=loc_name)
        except Exception:
            return redirect("/locations")
        return redirect("/locations")
    all_locations = Location.objects.all()
    return render(request, 'locations.html', context={'all_locations': all_locations})

def delete_location(request, location_id):
    location = Location.objects.get(pk=location_id)
    location.delete()
    return redirect("/locations")

def types_page(request: HttpRequest):
    if request.method == "POST":
        type_name = request.POST['type_name']
        try:
            Type.objects.create(name=type_name)
        except Exception:
            return redirect("/types")
        return redirect("/types")
    all_types = Type.objects.all()
    return render(request, 'types.html', context={'all_types': all_types})

def delete_type(request, type_id):
    type = Type.objects.get(pk=type_id)
    type.delete()
    return redirect("/types")

def basket_page(request: HttpRequest):
    all_products = Product.objects.all()
    if request.method == "POST":
        basket_product_name = request.POST['basket_product_name']
        basket_product_number = request.POST['basket_product_number']
        basket_product_comment = request.POST['basket_product_comment']
        try:
            product = Product.objects.get(name=basket_product_name)
            Basket.objects.create(name=product, number=basket_product_number, comment=basket_product_comment)
        except Exception:
            return redirect("/basket")
        return redirect("/basket")
    all_basket_products = Basket.objects.all()
    if not all_basket_products:
        status = 'Корзина пуста'
    else:
        status = ''
    return render(request, 'basket.html', context={'all_basket_products': all_basket_products, 'all_products': all_products, 'status': status})

def delete_basket_product(request, basket_product_id):
    basket_product = Basket.objects.get(pk=basket_product_id)
    basket_product.delete()
    return redirect("/basket")

def delete_all_basket_products(request):
    Basket.objects.all().delete()
    return redirect("/basket")

def make_basket(request):
    products_list = Product.objects.filter(necessity=True)
    purchases_list = Purchase.objects.all()
    purchases_names_list = []
    for purchase in purchases_list:
        purchases_names_list.append(purchase.name.name)
    for product in products_list:
        if product.name not in purchases_names_list:
            product_name = Product.objects.get(name=product.name)
            product_number = 1
            product_comment = ""
            try:
                if Basket.objects.get(name=product_name, number=product_number, comment=product_comment):
                    continue
            except Exception:
                Basket.objects.create(name=product_name, number=product_number, comment=product_comment)
    return redirect("/basket")

def edit_basket_product(request, basket_product_id):
    basket_product = Basket.objects.get(pk=basket_product_id)
    return render(request, 'basket_product.html', context={'basket_product': basket_product})

def edit_basket_product_page(request: HttpRequest, basket_product_id):
    basket_product = Basket.objects.get(pk=basket_product_id)
    all_products = Product.objects.all()
    if request.method == 'POST':
        basket_product_number = request.POST['basket_product_number']
        basket_product_comment = request.POST['basket_product_comment']
        try:
            # if basket_product_number == '' and basket_product_comment == '':
            #     return redirect ('/edit-basket-products/<basket_product_id>')
            if basket_product_number != '' and basket_product_comment == '':
                Basket.objects.update(number=basket_product_number)
            if basket_product_number == '' and basket_product_comment != '':
                Basket.objects.update(comment=basket_product_comment)
        except Exception:
            return render(request, 'basket_product.html', context={'basket_product': basket_product})
        return render(request, 'basket_product.html', context={'basket_product': basket_product})

    return render(request, 'basket_product.html', context={'basket_product': basket_product})

def products_page(request: HttpRequest):
    all_types = Type.objects.all()
    if request.method == "POST":
        product_name = request.POST['product_name']
        product_type = request.POST['product_type']
        product_necessity = bool(request.POST.get('product_necessity', False))
        try:
            product_type = Type.objects.get(name=product_type)
            Product.objects.create(name=product_name, type=product_type, necessity=product_necessity)
        except Exception:
            return redirect("/products")
        return redirect("/products")
    all_products = Product.objects.all()
    return render(request, 'products.html', context={'all_products': all_products, 'all_types': all_types})

def delete_product(request, product_id):
    product = Product.objects.get(pk=product_id)
    product.delete()
    return redirect("/products")

def purchases_page(request: HttpRequest):
    all_products = Product.objects.all()
    all_locations = Location.objects.all()
    if request.method == "POST":
        purchase_name = request.POST['purchase_name']
        purchase_date = request.POST['purchase_date']
        expiration_date = request.POST['expiration_date']
        purchase_number = request.POST['purchase_number']
        purchase_location = request.POST['purchase_location']
        purchase_comment = request.POST['purchase_comment']
        # try:
        if not expiration_date:
            expiration_date = None
        new_purchase_name = Product.objects.get(name=purchase_name)
        new_purchase_location = Location.objects.get(name=purchase_location)
        Purchase.objects.create(name=new_purchase_name, purchase_date=purchase_date, expiration_date=expiration_date, number=purchase_number, location=new_purchase_location, comment=purchase_comment)
        # except Exception:
        #     return redirect("/purchases")
        return redirect("/purchases")
    all_purchases = Purchase.objects.all()
    return render(request, 'purchases.html', context={'all_purchases': all_purchases, 'all_products': all_products, 'all_locations': all_locations})

def delete_purchase(request, purchase_id):
    purchase = Purchase.objects.get(pk=purchase_id)
    purchase.delete()
    return redirect("/purchases")