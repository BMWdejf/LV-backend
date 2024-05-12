from django.contrib import admin
from products.models import Products

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('fx_id', 'code', 'name', 'img_link', 'export_on_eshop')