from rest_framework import serializers

from .models import Category, Item


class CategorySerializer(serializers.ModelSerializer): 
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug']
        
        
class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'slug', 'name', 'img', 'category', 'price']