from django.shortcuts import render
from askor.models import *


def check_is_cat_empty():
    product_categories = ProductCategory.objects.filter(is_active=True)
    len_categories = len(product_categories)
    len_products = len(Product.objects.all())
    arr = []
    for i in Product.objects.all():
        if i.category.name not in arr:
            arr.append(i.category.name)
    try:
        last_category = arr[-1]
    except:
        last_category = 0
    return arr, last_category, product_categories, len_categories, len_products


def index(request):
    arr, last_category, product_categories, len_categories, len_products = check_is_cat_empty()
    return render(request, 'landing/index.html', locals())


def product(request,  product_category, product_id):
    arr, last_category, product_categories, len_categories, len_products = check_is_cat_empty()
    product = Product.objects.get(id=product_id)
    main_prod_img = ProductImage.objects.get(is_active=True, is_main=True, product__is_active=True, product_id=product_id)
    prod_cat = ProductCategory.objects.get(id=product_category)
    product.clicks += 1
    product.save()
    return render(request, 'landing/product.html', locals())


def info(request):
    arr, last_category, product_categories, len_categories, len_products = check_is_cat_empty()
    return render(request, 'landing/info.html', locals())


def contacs (request):
    arr, last_category, product_categories, len_categories, len_products = check_is_cat_empty()
    return render(request, 'landing/contacts.html', locals())


def product_catalog(request, product_category):
    arr, last_category, product_categories, len_categories, len_products = check_is_cat_empty()
    prod_cat = ProductCategory.objects.get(id=product_category)
    products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    products_images_category = products_images.filter(product__category__id=product_category).order_by('-product__clicks')
    return render(request, 'landing/product_catalog.html', locals())


def product_table(request, product_category):
    arr, last_category, product_categories, len_categories, len_products = check_is_cat_empty()
    prod_cat = ProductCategory.objects.get(id=product_category)
    all_cat_prod = Product.objects.filter(category=product_category)
    return render(request, 'landing/product-table.html', locals())