from django.urls import path

from . import views

app_name = 'administration'
urlpatterns = [
    path('products/', views.ProductIndex.as_view(), name='products'),
    path('product/create/', views.ProductCreate.as_view(), name='create-product'),
    path('product/<int:pk>/update/', views.ProductUpdate.as_view(), name='update-product'),
    path('product/<int:pk>/delete/', views.ProductDelete.as_view(), name='delete-product'),
    path('orders/', views.OrderIndex.as_view(), name='orders'),
    path('order/<int:pk>/', views.OrderDetail.as_view(), name='order-detail'),
    path('order/create', views.OrderCreate.as_view(), name='create-order'),
    path('order/<int:pk>/update/', views.OrderUpdate.as_view(), name='update-order'),
]
