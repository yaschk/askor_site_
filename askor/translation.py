# -*- coding: utf-8 -*-
from modeltranslation.translator import register, TranslationOptions
from .models import *

@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('product_name', 'in_stock', 'description',)


