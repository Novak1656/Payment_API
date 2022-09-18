from django.contrib import admin
from .models import Item


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price']
    list_display_links = ['id', 'name']
    list_filter = ['name', 'price']
    search_fields = ['name']
    save_on_top = True
    save_as = True
