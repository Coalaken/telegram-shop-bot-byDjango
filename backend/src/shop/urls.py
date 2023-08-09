from django.urls import path, include

from . import views


app_name = 'shop'


urlpatterns = [
    path('cats/', views.CategoryListAPIView.as_view(), name='cats'),
    path('items/', views.ItemListAPIView.as_view(), name='items'),
    path('delete/items/<int:item_id>/', views.ItemDeteilAPIView.as_view(), name='delete'),
    path('items/<cat_id>/', views.ItemByCategoryListAPIView.as_view(), name='by_category'),
    path('', include('cart.urls', namespace='cart'))
]
