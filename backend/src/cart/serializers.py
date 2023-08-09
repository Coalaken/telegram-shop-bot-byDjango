from rest_framework import serializers

from .models import Cart
from shop.seriaizers import ItemSerializer


class CartSerializer(serializers.ModelSerializer):
    products = ItemSerializer(many=True)
    class Meta:
        model = Cart
        fields = ('user_id', 'products')
