from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, Http404
from .models import Product


def index(request):
    all_product_list = Product.objects.all()
    template = loader.get_template('pricelist/index.html')
    context = { 'all_product_list' : all_product_list }
    return HttpResponse(template.render(context, request))

def detail(request, product_id):
    try:
        product = Product.objects.get(pk=product_id)
    except Product.DoesNotExist:
        raise Http404("Product does not exist")
    return render(request, 'pricelist/details.html', { 'product': product })

