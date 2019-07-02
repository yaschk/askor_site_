from django.shortcuts import render
from askor.models import *


def index(request):
    product_categories = ProductCategory.objects.all()
    len_products_images = len(product_categories)
    arr = []
    all_products = Product.objects.all()
    for i in all_products:
        if i.category.name not in arr:
            arr.append(i.category.name)
    last_category = arr[-1]
    return render(request, 'landing/index.html', locals())


def product(request,  product_category, product_id):
    product_categories = ProductCategory.objects.all()
    product = Product.objects.get(id=product_id)
    main_prod_img = ProductImage.objects.get(is_active=True, is_main=True, product__is_active=True, product_id=product_id)
    prod_cat = ProductCategory.objects.get(id=product_category)
    product.clicks += 1
    product.save()
    arr = []
    all_products = Product.objects.all()
    for i in all_products:
        if i.category.name not in arr:
            arr.append(i.category.name)
    last_category = arr[-1]
    return render(request, 'landing/product.html', locals())


def info(request):
    product_categories = ProductCategory.objects.all()
    arr = []
    all_products = Product.objects.all()
    for i in all_products:
        if i.category.name not in arr:
            arr.append(i.category.name)
    last_category = arr[-1]
    return render(request, 'landing/info.html', locals())


def contacs (request):
    product_categories = ProductCategory.objects.all()
    arr = []
    all_products = Product.objects.all()
    for i in all_products:
        if i.category.name not in arr:
            arr.append(i.category.name)
    last_category = arr[-1]
    return render(request, 'landing/contacts.html', locals())


def product_catalog(request, product_category):
    product_categories = ProductCategory.objects.all()
    prod_cat = ProductCategory.objects.get(id=product_category)
    products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    products_images_category = products_images.filter(product__category__id=product_category).order_by('-product__clicks')
    arr = []
    all_products = Product.objects.all()
    for i in all_products:
        if i.category.name not in arr:
            arr.append(i.category.name)
    last_category = arr[-1]
    return render(request, 'landing/product_catalog.html', locals())
