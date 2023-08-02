from django.urls import path

from . import views


app_name = 'shop'


urlpatterns = [
    path('cats/', views.CategoryListAPIView.as_view(), name='cats'),
    path('items/', views.ItemAPIView.as_view(), name='items'),
    path('items/<int:id>', views.ItemByCategoryListAPIView.as_view(), name='by_category')
]
