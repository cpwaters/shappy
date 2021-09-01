from django.shortcuts import render
from django.http import HttpResponse
from .models import Product


def index(request):
    all_product_list = Product.objects.all()
    output = ',<br>'.join([q.description for q in all_product_list])
    return HttpResponse(output)

def detail(request, product_id):
    return HttpResponse("%s" % product_id)

