from modeltranslation.translator import register, TranslationOptions
from .models import *


@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('product_name', 'in_stock', 'description', 'keywords',)

@register(ProductCategory)
class ProductCategoryTranslationOptions(TranslationOptions):
    fields = ('name',)