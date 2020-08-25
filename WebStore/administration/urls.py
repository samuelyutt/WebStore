from django.urls import path

from . import views

app_name = 'administration'
urlpatterns = [
    path('configuration/', views.ConfigurationDetail.as_view(), name='configuration'),
    path('configuration/update/', views.ConfigurationUpdate.as_view(), name='configuration_update'),
    
    path('product/', views.ProductIndex.as_view(), name='products'),
    path('product/create/', views.ProductCreate.as_view(), name='product_create'),
    path('product/<int:pk>/update/', views.ProductUpdate.as_view(), name='product_update'),
    path('product/<int:pk>/delete/', views.ProductDelete.as_view(), name='product_delete'),
    
    path('category/', views.CategoryIndex.as_view(), name='categories'),
    path('category/create/', views.CategoryCreate.as_view(), name='category_create'),
    path('category/<int:pk>/', views.CategoryDetail.as_view(), name='category_detail'),
    path('category/<int:pk>/update/', views.CategoryUpdate.as_view(), name='category_update'),
    path('category/<int:pk>/delete/', views.CategoryDelete.as_view(), name='category_delete'),
    
    path('order/', views.OrderIndex.as_view(), name='orders'),
    path('order/create/', views.OrderCreate.as_view(), name='order_create'),
    path('order/<int:pk>/', views.OrderDetail.as_view(), name='order_detail'),
    path('order/<int:pk>/update/', views.OrderUpdate.as_view(), name='order_update'),
    path('order/<int:order_id>/next_step/', views.order_next_step, name='order_next_step'),
]
