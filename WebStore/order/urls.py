from django.urls import path

from . import views

app_name = 'order'
urlpatterns = [
    path('cart/', views.cart, name='cart'),
    path('edit-cart-item/', views.cart_item_edit, name='edit_cart_item'),
    path('<int:product_id>/edit-cart-item/', views.cart_item_edit, name='edit_cart_item'),
    path('<int:order_id>/', views.order_detail, name='detail'),
    path('create/', views.order_create, name='create'),
    path('next-step/', views.next_step, name='next_step'),
]
