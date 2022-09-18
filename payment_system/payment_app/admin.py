from django.contrib import admin
from .models import Item, Discount, Order


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price']
    list_display_links = ['id', 'name']
    list_filter = ['name', 'price']
    search_fields = ['name']
    save_on_top = True
    save_as = True


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'discount', 'created_at', 'updated_at']
    list_display_links = ['id', 'name']
    list_filter = ['created_at']
    search_fields = ['name']
    save_on_top = True
    save_as = True


@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'discount_value']
    list_display_links = ['id', 'name']
    list_filter = ['discount_value']
    search_fields = ['name']
    save_on_top = True
    save_as = True
