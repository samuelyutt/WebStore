from django.http import HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.utils import timezone
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.mixins import UserPassesTestMixin

from .models import Configuration
from products.models import Category, Product
from order.models import Order, Promo

# Create your views here.
class StaffMemberRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff

############ CONFIGURATION ############
class ConfigurationDetail(StaffMemberRequiredMixin, generic.DetailView):
    model = Configuration
    template_name = 'administration/configuration_detail.html'

    def get_object(self):
        return Configuration.objects.first()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_configuration'] = 'active'
        context['subactive_configuration'] = 'active'
        return context

class ConfigurationUpdate(StaffMemberRequiredMixin, generic.UpdateView):
    model = Configuration
    template_name = 'administration/configuration_update_form.html'
    fields = ['site_name', 'is_visitable', 'site_logo_small', 'site_logo_large', 'is_sellable', 'manager_bank_code', 'manager_bank_name', 'manager_receiving_account_name', 'manager_receiving_account', 'shipping_fee', 'discount_shipping_fee', 'manager_name', 'manager_contact_phone_no', 'manager_email', 'manager_address']

    def get_object(self):
        return Configuration.objects.first()
    
    def get_success_url(self):
        return reverse('administration:configuration')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_configuration'] = 'active'
        context['subactive_configuration'] = 'active'
        return context

############ CATEGORIES ############
class CategoryIndex(StaffMemberRequiredMixin, generic.ListView):
    template_name = 'administration/category_index.html'

    def get_queryset(self):
        return Category.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_products'] = 'active'
        context['subactive_cat_all'] = 'active'
        return context

class CategoryDetail(StaffMemberRequiredMixin, generic.DetailView):
    model = Category
    template_name = 'administration/category_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_products'] = 'active'
        return context

class CategoryCreate(StaffMemberRequiredMixin, generic.CreateView):
    model = Category
    template_name = 'administration/category_form.html'
    fields = ['name',]
    
    def get_success_url(self):
        return reverse('administration:categories')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_products'] = 'active'
        context['subactive_cat_create'] = 'active'
        return context

class CategoryUpdate(StaffMemberRequiredMixin, generic.UpdateView):
    model = Category
    template_name = 'administration/category_update_form.html'
    fields = ['name',]
    
    def get_success_url(self):
        return reverse('administration:categories')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_products'] = 'active'
        return context

class CategoryDelete(StaffMemberRequiredMixin, generic.DeleteView):
    model = Category
    template_name = 'administration/category_confirm_delete.html'
    success_url = reverse_lazy('administration:categories')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_products'] = 'active'
        return context


############ PRODUCTS ############
class ProductIndex(StaffMemberRequiredMixin, generic.ListView):
    template_name = 'administration/product_index.html'

    def get_queryset(self):
        return Product.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_products'] = 'active'
        context['subactive_all'] = 'active'
        return context

class ProductCreate(StaffMemberRequiredMixin, generic.CreateView):
    model = Product
    template_name = 'administration/product_form.html'
    fields = ['category', 'name', 'unit_price', 'utility', 'ingredient', 'description', 'is_sellable', 'inventory_quantity', 'cover_image']
    
    def get_success_url(self):
        return reverse('administration:products')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_products'] = 'active'
        context['subactive_create'] = 'active'
        return context

class ProductUpdate(StaffMemberRequiredMixin, generic.UpdateView):
    model = Product
    template_name = 'administration/product_update_form.html'
    fields = ['category', 'name', 'unit_price', 'utility', 'ingredient', 'description', 'is_sellable', 'inventory_quantity', 'cover_image']
    
    def get_success_url(self):
        return reverse('administration:products')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_products'] = 'active'
        return context

class ProductDelete(StaffMemberRequiredMixin, generic.DeleteView):
    model = Product
    template_name = 'administration/product_confirm_delete.html'
    success_url = reverse_lazy('administration:products')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_products'] = 'active'
        return context


############ ORDER ############
class OrderIndex(StaffMemberRequiredMixin, generic.ListView):
    model = Order
    template_name = 'administration/order_index.html'

    def get_queryset(self):
        return reversed(Order.objects.all())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_orders'] = 'active'
        context['subactive_all'] = 'active'
        return context

class OrderDetail(StaffMemberRequiredMixin, generic.DetailView):
    model = Order
    template_name = 'administration/order_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_orders'] = 'active'
        return context

class OrderCreate(StaffMemberRequiredMixin, generic.CreateView):
    model = Order
    template_name = 'administration/order_form.html'
    fields = ['user', 'user_name', 'user_gender', 'user_contact_phone_no', 'shipping_postal_code', 'shipping_address', 'shipping_fee', 'total_amount', 'status', 'payment', 'remittance_account']
    
    def get_success_url(self):
        return reverse('administration:orders')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_orders'] = 'active'
        context['subactive_create'] = 'active'
        return context

class OrderUpdate(StaffMemberRequiredMixin, generic.UpdateView):
    model = Order
    template_name = 'administration/order_update_form.html'
    fields = ['user', 'user_name', 'user_gender', 'user_contact_phone_no', 'shipping_postal_code', 'shipping_address', 'shipping_fee', 'total_amount', 'status', 'payment', 'remittance_account']    
    
    def get_success_url(self):
        return reverse('administration:orders')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_orders'] = 'active'
        return context

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


class PromoIndex(StaffMemberRequiredMixin, generic.ListView):
    model = Promo
    template_name = 'administration/promo_index.html'

    def get_queryset(self):
        return reversed(Promo.objects.all())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_promo'] = 'active'
        context['subactive_all'] = 'active'
        return context

class PromoDetail(StaffMemberRequiredMixin, generic.DetailView):
    model = Promo
    template_name = 'administration/promo_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_promo'] = 'active'
        return context

class PromoCreate(StaffMemberRequiredMixin, generic.CreateView):
    model = Promo
    template_name = 'administration/promo_form.html'
    fields = ['code', 'discount_type', 'has_total_amount_limit', 'has_total_count_limit', 'has_time_limit']
    
    def get_success_url(self):
        return reverse('administration:promo_content_update', args=[self.object.id])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_promo'] = 'active'
        context['subactive_create'] = 'active'
        return context

class PromoTypeUpdate(StaffMemberRequiredMixin, generic.UpdateView):
    model = Promo
    template_name = 'administration/promo_update_form.html'
    fields = ['code', 'discount_type', 'has_total_amount_limit', 'has_total_count_limit', 'has_time_limit']
    
    def get_success_url(self):
        return reverse('administration:promo_content_update', args=[self.object.id])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_promo'] = 'active'
        context['next'] = '下一步'
        return context

class PromoContentUpdate(StaffMemberRequiredMixin, generic.UpdateView):
    model = Promo
    template_name = 'administration/promo_update_form.html'
    fields = []    
    
    def get_success_url(self):
        return reverse('administration:promos')

    def dispatch(self, request, *args, **kwargs):
        promo = super().get_object()
        self.fields = []
        
        # Discount Type
        if promo.discount_type == 0:
            self.fields += ['discount_amount']
        elif promo.discount_type == 1:
            self.fields += ['discount_ratio', 'discount_limit']

        # Limitations
        if promo.has_total_amount_limit == 1:
            self.fields += ['total_amount_limit']

        if promo.has_total_count_limit == 1:
            self.fields += ['total_count_limit']

        if promo.has_time_limit == 1:
            self.fields += ['time_limit_start', 'time_limit_expire']
        
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_promo'] = 'active'
        context['next'] = '完成'
        return context