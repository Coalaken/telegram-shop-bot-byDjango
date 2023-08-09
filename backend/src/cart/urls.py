from django.urls import path 

from . import views


app_name = 'cart'


urlpatterns = [
    path('cart/<int:user_id>/', views.get_user_cart, name='cart'),
    path('cart/add/<int:user_id>/<int:product_id>/', views.add_to_cart, name='add'),
    path('cart/del/<int:user_id>/<int:product_id>/', views.delete_from_cart, name='delete')
]
