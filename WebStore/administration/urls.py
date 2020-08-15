from django.urls import path

from . import views

app_name = 'administration'
urlpatterns = [
    path('product/', views.ProductIndex.as_view(), name='products'),
    path('product/create/', views.ProductCreate.as_view(), name='product_create'),
    path('product/<int:pk>/update/', views.ProductUpdate.as_view(), name='product_update'),
    path('product/<int:pk>/delete/', views.ProductDelete.as_view(), name='product_delete'),
    path('order/', views.OrderIndex.as_view(), name='orders'),
    path('order/create/', views.OrderCreate.as_view(), name='order_create'),
    path('order/<int:pk>/', views.OrderDetail.as_view(), name='order_detail'),
    path('order/<int:pk>/update/', views.OrderUpdate.as_view(), name='order_update'),
    path('order/<int:order_id>/confirm-paid/', views.order_confirm_paid, name='order_confirm_paid'),
]
