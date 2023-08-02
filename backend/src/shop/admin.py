from django.contrib import admin

from .models import Category, Item


@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_editable = ['name']
    search_fields = ['name']
    
    
@admin.register(Item)
class AdminItem(admin.ModelAdmin):
    list_display = ['id', 'name', 'category', 'price', 'description']
    list_filter = ['price']
    search_fields = ['name', 'description']
    list_editable = ['name', 'description', 'price']
    raw_id_fields = ['category']