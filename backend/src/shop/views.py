from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.views.decorators.http import require_POST

from .models import Category, Item
from .seriaizers import ItemSerializer, CategorySerializer


class CategoryListAPIView(APIView):
    def get(self, request, *args, **kwargs) -> Response:
        try:
            data = Category.objects.all()
            serializer_data = CategorySerializer(data, many=True).data
            return Response(serializer_data, status=status.HTTP_200_OK)
        except (Exception, Category.DoesNotExist):
            return Response({'message': 'Empty'}, status=status.HTTP_400_BAD_REQUEST) 
        
    def post(self, request, *args, **kwargs) -> Response:
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class ItemListAPIView(APIView):
    
    def get(self, request, *args, **kwargs) -> Response:
        try:
            data = Item.objects.all().select_related('category')
            serializer_data = ItemSerializer(data, many=True).data
            return Response(serializer_data, status=status.HTTP_200_OK)
        except (Exception, Item.DoesNotExist):
            return Response({'message': 'Empty'}, status=status.HTTP_400_BAD_REQUEST) 
        
    def post(self, request, *args, **kwargs) -> Response:
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    
class ItemDeteilAPIView(APIView):
    
    def _get_item(self, item_id) -> Item:
        try:
            return Item.objects.get(id=item_id)
        except Item.DoesNotExist:
            return Response({'message': 'Something wrong'}, status=status.HTTP_404_NOT_FOUND)
    
    def get(self, request, item_id) -> Response:
        item = self._get_item(item_id)
        serializer = ItemSerializer(item, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK) 
    
    def delete(self, request, item_id) -> Response:
        item = self._get_item(item_id)
        item.delete()
        return Response({'message': 'Deleted'}, status=status.HTTP_204_NO_CONTENT)
    
    
class ItemByCategoryListAPIView(APIView):
    def get(self, request, cat_id, *args, **kwargs) -> Response:
        try:
            data = Item.objects.filter(category__id=cat_id)
            serializer_data = ItemSerializer(data, many=True).data
            return Response(serializer_data, status=status.HTTP_200_OK)
        except Category.DoesNotExist:
            return Response({'message': 'Empty'}, status=status.HTTP_400_BAD_REQUEST) 