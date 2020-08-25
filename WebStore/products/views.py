from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Product
from administration.models import Configuration

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'products/index.html'

    def get_queryset(self):
        return Product.objects.filter(is_sellable=True)

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['config'] = Configuration.objects.first()
        return context

class DetailView(generic.DetailView):
    model = Product
    template_name = 'products/detail.html'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        context['config'] = Configuration.objects.first()
        return context

    