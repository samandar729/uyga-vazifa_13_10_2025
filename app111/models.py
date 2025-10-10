from django.db import models

class categories(models.Model):
    category_name=models.CharField(max_length=100)
    descriptio=models.CharField(max_length=100)
    picture=models.ImageField(upload_to='pictures/%Y/%m/%d', blank=True, null=True)


    def __str__(self):
        return self.category_name

class products(models.Model):
    product_name=models.CharField(max_length=100)
    unit_price=models.CharField(max_length=100)
    discontinued=models.CharField(max_length=100)
    category_id=models.ForeignKey(categories, on_delete=models.CASCADE, default=1)

class orders(models.Model):
    order_date=models.DateTimeField(auto_now_add=True, verbose_name='add_date')
    requirid_date=models.DateTimeField(auto_now_add=True, verbose_name='add_date')
    shipped_date=models.DateTimeField(auto_now=True)

class order_details(models.Model):
    unit_price=models.CharField(max_length=100)
    quantity=models.CharField(max_length=100)
    order_id=models.ForeignKey(orders, on_delete=models.CASCADE, default=1)
    product_id=models.ForeignKey(products, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.category_name
