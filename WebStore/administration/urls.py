from django.urls import path

from . import views

app_name = 'administration'
urlpatterns = [
    path('products/', views.ProductIndex.as_view(), name='products'),
    path('create-product/', views.ProductCreate.as_view(), name='create-product'),
    path('<int:pk>/update-product/', views.ProductUpdate.as_view(), name='update-product'),
    path('<int:pk>/delete-product/', views.ProductDelete.as_view(), name='delete-product'),
]
