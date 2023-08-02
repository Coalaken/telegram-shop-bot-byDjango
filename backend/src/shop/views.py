from rest_framework.views import View
from rest_framework.response import Response
from rest_framework import status

from .models import Category, Item
from .seriaizers import ItemSerializer, CategorySerializer


class CategoryListAPIView(View):
    def get(self, request, *args, **kwargs):
        try:
            data = Category.objects.all()
            serializer_data = CategorySerializer(data, many=True).data
            return Response(serializer_data, status=status.HTTP_200_OK)
        except (Exception, Category.DoesNotExist):
            return Response({'message': 'Empty'}, status=status.HTTP_400_BAD_REQUEST) 
        

class ItemAPIView(View):
    def get(self, request, *args, **kwargs):
        try:
            data = Item.objects.all().select_related('category')
            serializer_data = CategorySerializer(data, many=True).data
            return Response(serializer_data, status=status.HTTP_200_OK)
        except (Exception, Item.DoesNotExist):
            return Response({'message': 'Empty'}, status=status.HTTP_400_BAD_REQUEST) 
        

class ItemByCategoryListAPIView(View):
    def get(self, id, request, *args, **kwargs):
        try:
            data = Item.objects.filter(category__id=id)
            serializer_data = CategorySerializer(data, many=True).data
            return Response(serializer_data, status=status.HTTP_200_OK)
        except Category.DoesNotExist:
            return Response({'message': 'Empty'}, status=status.HTTP_400_BAD_REQUEST) 