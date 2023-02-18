from django.db import models

class Type(models.Model):
    name = models.CharField(max_length=80, blank=False, unique=True)

    def __str__(self) -> str:
        return f'{self.name}'

class Location(models.Model):
    name = models.CharField(max_length=80, blank=False, unique=True)

    def __str__(self) -> str:
        return f'{self.name}'

class ProductService:
    @staticmethod
    def get_all_sorted_by_name():
        return Product.objects.order_by("name").all()

class Product(models.Model):
    name = models.CharField(max_length=200, blank=False, unique=True)
    necessity = models.BooleanField(blank=False)
    type = models.ForeignKey(Type, on_delete=models.SET_DEFAULT, default='')

    def __str__(self) -> str:
        if self.necessity == True:
            necessity = '🟢'
        if self.necessity == False:
            necessity = '🟡'
        return f'{self.name}, {self.type}, {necessity}'

class Basket(models.Model):
    name = models.ForeignKey(Product, on_delete=models.CASCADE)
    number = models.IntegerField(default=1)
    comment = models.CharField(max_length=200, blank=True)

    def __str__(self) -> str:
        return f'{self.name.name}, {self.number}, {self.comment}'

class Purchase(models.Model):
    name = models.ForeignKey(Product, on_delete=models.CASCADE)
    purchase_date = models.DateField(blank=False)
    expiration_date = models.DateField(blank=True, null=True)
    number = models.IntegerField(blank=False, default=1)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)
    comment = models.CharField(max_length=200, blank=True)
    
    def __str__(self) -> str:
        if self.expiration_date is None:
            self.expiration_date = '-'
        return f'{self.name.name}, дата покупки: {self.purchase_date}, срок годности: {self.expiration_date}, количество: {self.number}, место хранения: {self.location}. ({self.comment})'
