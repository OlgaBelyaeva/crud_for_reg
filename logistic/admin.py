from django.contrib import admin

# Register your models here.
from logistic.models import StockProduct, Product, Stock


class StockProductInline(admin.TabularInline):
    model = StockProduct
    extra = 0

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description']
    list_filter = ['id', 'title']
    inlines = [StockProductInline, ]

@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ['id', 'address'] # если добавляю products, то начинает ругаться, что тут не должно быть м2м
    list_filter = ['id', 'address']
    inlines = [StockProductInline, ]




