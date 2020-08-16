from django.http import HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.utils import timezone
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.mixins import UserPassesTestMixin

from .models import Settings
from products.models import Product
from order.models import Order

# Create your views here.
############ PRODUCTS ############
class StaffMemberRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff

class ProductIndex(StaffMemberRequiredMixin, generic.ListView):
    template_name = 'administration/product_index.html'

    def get_queryset(self):
        return Product.objects.all()

class ProductCreate(StaffMemberRequiredMixin, generic.CreateView):
    model = Product
    template_name = 'administration/product_form.html'
    fields = ['category', 'name', 'unit_price', 'utility', 'ingredient', 'description', 'is_sellable', 'inventory_quantity', 'cover_image']
    
    def get_success_url(self):
        return reverse('administration:products')

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['activate'] = 'location'
    #     return context

class ProductUpdate(StaffMemberRequiredMixin, generic.UpdateView):
    model = Product
    template_name = 'administration/product_update_form.html'
    fields = ['category', 'name', 'unit_price', 'utility', 'ingredient', 'description', 'is_sellable', 'inventory_quantity', 'cover_image']
    
    def get_success_url(self):
        return reverse('administration:products')

class ProductDelete(StaffMemberRequiredMixin, generic.DeleteView):
    model = Product
    template_name = 'administration/product_confirm_delete.html'
    success_url = reverse_lazy('administration:products')


############ ORDER ############
class OrderIndex(StaffMemberRequiredMixin, generic.ListView):
    template_name = 'administration/order_index.html'

    def get_queryset(self):
        return Order.objects.all()

class OrderDetail(StaffMemberRequiredMixin, generic.DetailView):
    model = Order
    template_name = 'administration/order_detail.html'

class OrderCreate(StaffMemberRequiredMixin, generic.CreateView):
    model = Order
    template_name = 'administration/order_form.html'
    fields = ['user', 'user_name', 'user_gender', 'user_contact_phone_no', 'shipping_postal_code', 'shipping_address', 'shipping_fee', 'total_amount', 'status', 'payment', 'remittance_account', 'is_canceled']
    
    def get_success_url(self):
        return reverse('administration:orders')

class OrderUpdate(StaffMemberRequiredMixin, generic.UpdateView):
    model = Order
    template_name = 'administration/order_update_form.html'
    fields = ['user', 'user_name', 'user_gender', 'user_contact_phone_no', 'shipping_postal_code', 'shipping_address', 'shipping_fee', 'total_amount', 'status', 'payment', 'remittance_account', 'is_canceled']    
    
    def get_success_url(self):
        return reverse('administration:orders')

# class OrderDelete(StaffMemberRequiredMixin, generic.DeleteView):
#     model = Order
#     template_name = 'administration/order_confirm_delete.html'
#     success_url = reverse_lazy('administration:orders')

@staff_member_required
def order_next_step(request, order_id):
    try:
        order = None
        try:
            order = Order.objects.get(id=order_id)
        except:
            raise Http404
        
        next_status = int(request.POST.get('next_status', order.status))
        order.status = next_status if order.status < next_status else order.status
        order.save()
        
        current_page = request.POST.get('current_page', 'orders')
        if current_page == 'order_detail':
            return HttpResponseRedirect(reverse('administration:order_detail', args=[order_id]))
        else:
            return HttpResponseRedirect(reverse('administration:orders'))
    except:
        return HttpResponseRedirect(reverse('products:index')) #home
