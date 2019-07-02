from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin


class ProductCategoryAdmin (TranslationAdmin):
    list_display = [field.name for field in ProductCategory._meta.fields]
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }
    class Meta:
        model = ProductCategory


admin.site.register(ProductCategory, ProductCategoryAdmin)


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 0


class ProductAdmin (TranslationAdmin):
    list_display = [field.name for field in Product._meta.fields]
    inlines = [ProductImageInline]
    search_fields = ["product_name"]
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }
    class Meta:
        model = Product


admin.site.register(Product, ProductAdmin)


class ProductImageAdmin (admin.ModelAdmin):
    list_display = [field.name for field in ProductImage._meta.fields]


    class Meta:
        model = ProductImage


admin.site.register(ProductImage, ProductImageAdmin)
