from django.urls import path

from . import views

app_name = 'order'
urlpatterns = [
    path('cart/', views.cart, name='cart'),
    path('add-to-cart/', views.add_to_cart, name='add_to_cart'),
]
