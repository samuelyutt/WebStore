from django.urls import path

from . import views

app_name = 'administration'
urlpatterns = [
    path('product/', views.ProductIndex.as_view(), name='products'),
    path('product/create/', views.ProductCreate.as_view(), name='create_product'),
    path('product/<int:pk>/update/', views.ProductUpdate.as_view(), name='update_product'),
    path('product/<int:pk>/delete/', views.ProductDelete.as_view(), name='delete_product'),
    path('order/', views.OrderIndex.as_view(), name='orders'),
    path('order/create/', views.OrderCreate.as_view(), name='create_order'),
    path('order/<int:pk>/', views.OrderDetail.as_view(), name='order_detail'),
    path('order/<int:pk>/update/', views.OrderUpdate.as_view(), name='update_order'),
    path('order/<int:order_id>/confirm-paid/', views.order_confirm_paid, name='order_confirm_paid'),
]
