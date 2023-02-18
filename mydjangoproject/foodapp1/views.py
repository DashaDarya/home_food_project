from django.shortcuts import render
from django.shortcuts import redirect
from foodapp1.models import Location, Type, Basket, Product, Purchase, ProductService
from django.http.request import HttpRequest
import datetime

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

def return_to_locations_page(request):
    return redirect('/locations')

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

def return_to_types_page(request):
    return redirect('/types')

def basket_page(request: HttpRequest):
    all_products = ProductService.get_all_sorted_by_name()
    if request.method == "POST" and 'purchased' in request.POST:
        add_purchases_from_basket(request)

    if request.method == "POST" and 'post' in request.POST:
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

def return_to_products_page(request):
    return redirect('/products')

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
    print(basket_product.number, basket_product.comment)
    if request.method == 'POST':
        basket_product_number = request.POST['basket_product_number']
        basket_product_comment = request.POST['basket_product_comment']
        
        try:
            if basket_product_number != '' and basket_product_comment == '':
                basket_product.number = basket_product_number
                basket_product.save()
            if basket_product_number == '' and basket_product_comment != '':
                basket_product.comment = basket_product_comment
                basket_product.save()
            if basket_product_number != '' and basket_product_comment != '':
                basket_product.number = basket_product_number
                basket_product.comment = basket_product_comment
                basket_product.save()
        except Exception:
            return render(request, 'basket_product.html', context={'basket_product': basket_product})
        return render(request, 'basket_product.html', context={'basket_product': basket_product})
    return render(request, 'basket_product.html', context={'basket_product': basket_product})

def return_to_basket(request):
    return redirect("/basket")

def add_purchases_from_basket(request: HttpRequest):
    checked_basket_products_id = request.POST.getlist('checks[]')
    print(checked_basket_products_id)
    print('куплено')
    for basket_product_id in checked_basket_products_id:
        basket_product = Basket.objects.get(id=basket_product_id)
        product_name = basket_product.name.name
        product_name = Product.objects.get(name=product_name)
        product_number = basket_product.number
        product_purchase_date = datetime.date.today()
        product_location = Location.objects.get(name='Стол')
        product_comment = basket_product.comment
        Purchase.objects.create(name=product_name, purchase_date=product_purchase_date, number=product_number, location=product_location, comment=product_comment)
        basket_product.delete()
    return redirect("/basket")

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
    
    all_products = Product.objects.select_related("type").order_by("-necessity").order_by("type__name").all()

    return render(request, 'products.html', context={'all_products': all_products, 'all_types': all_types})

def delete_product(request, product_id):
    product = Product.objects.get(pk=product_id)
    product.delete()
    return redirect("/products")
    
def purchases_page(request: HttpRequest):
    all_products = Product.objects.all()
    all_locations = Location.objects.all()
    all_types = Type.objects.all()
    if request.method == "POST" and 'location_search_submit' in request.POST:
        location_name = request.POST['location_search_name']
        location_search = Location.objects.get(name=location_name)
        products = Purchase.objects.filter(location=location_search).all()

        for prodcut in products:
            if prodcut.expiration_date is None:
                prodcut.expiration_date = "-"
        return render(request, 'location_search.html', context={'location': location_name, 'products': products})

    if request.method == "POST" and 'type_search_submit' in request.POST:
        type_name = request.POST['type_search_name']
        # type_search = Type.objects.get(name=type_name)
        products = Product.objects.filter(type__name=type_name)
        purchases = Purchase.objects.filter(name__in=products)
        return render(request, 'type_search.html', context={'products': purchases, 'type': type_name})

    if request.method == "POST" and 'new_purchase_submit' in request.POST:
        purchase_name = request.POST['purchase_name']
        purchase_date = request.POST['purchase_date']
        expiration_date = request.POST['expiration_date']
        purchase_number = request.POST['purchase_number']
        purchase_location = request.POST['purchase_location']
        purchase_comment = request.POST['purchase_comment']
        try:
            if not expiration_date:
                expiration_date = None
            new_purchase_name = Product.objects.get(name=purchase_name)
            new_purchase_location = Location.objects.get(name=purchase_location)
            Purchase.objects.create(name=new_purchase_name, purchase_date=purchase_date, expiration_date=expiration_date, number=purchase_number, location=new_purchase_location, comment=purchase_comment)
        except Exception:
            return redirect("/purchases")
        return redirect("/purchases")
    all_purchases = Purchase.objects.all()
    return render(request, 'purchases.html', context={'all_purchases': all_purchases, 'all_products': all_products, 'all_locations': all_locations, 'all_types': all_types})

def delete_purchase(request, purchase_id):
    purchase = Purchase.objects.get(pk=purchase_id)
    purchase.delete()
    return redirect("/purchases")

def edit_purchase(request: HttpRequest, purchase_id):
    purchase = Purchase.objects.get(pk=purchase_id)
    all_locations = Location.objects.all()
    # print(basket_product.number, basket_product.comment)
    if request.method == 'POST':
        purchase_date = request.POST['purchase_date']
        purchase_expiration_date = request.POST['purchase_expiration_date']
        purchase_number = request.POST['purchase_number']
        purchase_location = request.POST['purchase_location']
        purchase_comment = request.POST['purchase_comment']
        delete_expiration_date = bool(request.POST.get('delete_expiration_date', False))
        
        
        print(purchase_location)

        try:
            if  purchase_date != '':
                purchase.purchase_date = purchase_date
            if purchase_expiration_date != '':
                purchase.expiration_date = purchase_expiration_date
            if delete_expiration_date == True:
                purchase.expiration_date = None
            if purchase_number != '':
                purchase.number = purchase_number
            if purchase_location != '- Не выбрано -':
                purchase_location = Location.objects.get(name=purchase_location)
                purchase.location = purchase_location
            if purchase_comment != '':
                purchase.comment = purchase_comment
            purchase.save()
        except Exception:
            return render(request, 'purchase.html', context={'purchase': purchase, 'all_locations': all_locations})
        return render(request, 'purchase.html', context={'purchase': purchase, 'all_locations': all_locations})
    return render(request, 'purchase.html', context={'purchase': purchase, 'all_locations': all_locations})

def return_to_purchases(request):
    return redirect("/purchases")

def show_expired(request):
    current_date = datetime.date.today()
    expired_purchases = Purchase.objects.filter(expiration_date__lt=current_date)
    print(expired_purchases)
    return render(request, 'expired_purchases.html', context={'expired_purchases': expired_purchases})

def show_old(request):
    current_date = datetime.date.today()
    delta = datetime.timedelta(31)
    month_earlier = current_date - delta
    print(month_earlier)
    p = Product.objects.get(name='Мука')
    old_products = Purchase.objects.filter(purchase_date__lt=month_earlier).exclude(name=p).filter(expiration_date=None)
    return render(request, 'old_products.html', context={'old_products': old_products})
