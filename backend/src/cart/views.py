from rest_framework import status
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

from shop.models import Item
from .models import Cart
from .serializers import CartSerializer


def get_cart(user_id: int) -> Cart:
    cart, _ = Cart.objects.get_or_create(user_id=user_id)
    return cart


@api_view(['POST'])
def add_to_cart(request, user_id, product_id) -> Response:
    cart = get_cart(user_id)    
    cart.products.add(product_id)
    cart.save()
    return Response({'cart': cart.products.values_list('id', flat=True)}, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_user_cart(request, user_id) -> Response:
    cart = get_cart(user_id)
    serializer_data = CartSerializer(cart, many=False).data
    return Response(serializer_data, status=status.HTTP_200_OK)


@api_view(['DELETE'])
def delete_from_cart(request, user_id: int, product_id: int) -> Response:
    product = get_object_or_404(Item, id=product_id)
    cart = get_cart(user_id)
    cart.products.remove(product)
    cart.save()
    return Response({'message': f'deleted, id: {product.id}'}, status=status.HTTP_204_NO_CONTENT)
