from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.utils import timezone
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.mixins import UserPassesTestMixin

from .models import Settings
from products.models import Product

# Create your views here.
class StaffMemberRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff

class ProductIndex(StaffMemberRequiredMixin, generic.ListView):
    template_name = 'administration/product_index.html'

    def get_queryset(self):
        return Product.objects.all()

class ProductCreate(StaffMemberRequiredMixin, generic.CreateView):
    model = Product
    fields = ['category', 'name', 'unit_price', 'utility', 'ingredient', 'description', 'is_unit_sellable', 'inventory_quantity']
    
    def get_success_url(self):
        return reverse('administration:products')

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['activate'] = 'location'
    #     return context

class ProductUpdate(StaffMemberRequiredMixin, generic.UpdateView):
    model = Product
    fields = ['category', 'name', 'unit_price', 'utility', 'ingredient', 'description', 'is_unit_sellable', 'inventory_quantity']
    
    def get_success_url(self):
        return reverse('administration:products')

class ProductDelete(StaffMemberRequiredMixin, generic.DeleteView):
    model = Product
    success_url = reverse_lazy('administration:products')