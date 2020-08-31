from django.urls import path

from . import views

app_name = 'order'
urlpatterns = [
    path('cart/', views.cart, name='cart'),
    path('cart-item-edit/', views.cart_item_edit, name='cart_item_edit'),
    path('<int:product_id>/edit-cart-item/', views.cart_item_edit, name='cart_item_edit'),
    path('', views.IndexView.as_view(), name='index'),
    # path('<int:order_id>/', views.order_detail, name='detail'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('create/', views.order_create, name='create'),
    path('next-step/', views.next_step, name='next_step'),
    path('<int:pk>/edit-remittance-account/', views.EditRemittanceAccount.as_view(), name='edit_remittance_account'),
    path('<int:order_id>/promo-apply/', views.promo_apply, name='promo_apply'),
    path('<int:order_id>/promo-remove/', views.promo_remove, name='promo_remove'),
]
