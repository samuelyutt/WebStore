"""WebStore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('accounts/', include('django.contrib.auth.urls')),
    path('auth/', views.customer_login, name='customer_login'),
    path('auth/create/', views.customer_create, name='customer_create'),
    path('auth/logout/', views.user_logout, name='logout'),
    path('auth/me/', views.profile, name='profile'),
    path('auth/me/update', views.profile_update, name='profile_update'),
    path('auth/me/update-password', views.password_update, name='password_update'),
    
    path('administration/', include('administration.urls')),

    # path('', views.user_logout, name='home'),
    path('products/', include('products.urls')),
    path('order/', include('order.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
