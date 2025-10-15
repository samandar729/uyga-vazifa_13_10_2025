from django.shortcuts import render
from .models import *

def index(request):
    cat=categories.objects.all()
    ppp=products.objects.all()
    ooo=orders.objects.all()
    ord=order_details.objects.all()
    content={
        "cat":cat,
        "ppp":ppp,
        "ooo":ooo,
        "ord":ord
    }
    return render(request,'index.html',content)
