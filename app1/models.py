
from django.db import models

class categories(models.Model):
    category_name=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    picture=models.ImageField(upload_to='pictures/%Y/%m/%d', blank=True, null=True)


    def __str__(self):
        return self.category_name

class products(models.Model):
    product_name=models.CharField(max_length=100)
    unit_price=models.CharField(max_length=100)
    discontinued=models.CharField(max_length=100)
    category_id=models.ForeignKey(categories, on_delete=models.CASCADE, default=1)

class orders(models.Model):
    order_date = models.DateTimeField(auto_now_add=True)
    required_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    shipped_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)



class order_details(models.Model):
    unit_price=models.CharField(max_length=100)
    quantity=models.CharField(max_length=100)
    order_id=models.ForeignKey(orders, on_delete=models.CASCADE, default=1)
    product_id=models.ForeignKey(products, on_delete=models.CASCADE, default=1)

class Suppliers(models.Model):
    company_name=models.CharField(max_length=100)
    contact_name = models.CharField(max_length=100)
    contact_title = models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    region=models.CharField(max_length=100)
    postal_code=models.CharField(max_length=5)
    country=models.CharField(max_length=15)
    phone=models.CharField(max_length=10)
    fax=models.CharField(max_length=30)
    homepage=models.CharField(max_length=50)

    def __str__(self):
        return self.company_name

    def __str__(self):
        return self.product_id.product_name
