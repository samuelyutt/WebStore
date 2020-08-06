from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Product

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'products/index.html'

    def get_queryset(self):
        return Product.objects.all()


class DetailView(generic.DetailView):
    model = Product
    template_name = 'products/detail.html'
    
    def get_queryset(self):
        return Product.objects.all()

    