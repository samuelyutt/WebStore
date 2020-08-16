from django.http import HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User

from products.models import Product
from .models import CartItem, OrderItem, Order


# Create your views here.
@login_required
def cart(request):
    context = {}
    context['cart_items'] = request.user.cartitem_set.all()
    for item in context['cart_items']:
        if not item.is_valid():
            context['is_not_valid'] = True
            break
    return render(request, 'order/cart.html', context)

@login_required
def cart_item_edit(request, product_id=0):
    try:
        user = request.user
        product = Product.objects.get(id=int(request.POST.get('product_id', product_id)))
        amount = int(request.POST.get('amount', 1))
        cart_item = None

        try:
            cart_item = user.cartitem_set.get(product=product)
            cart_item.amount += amount
        except:
            cart_item = CartItem(user=user, product=product, amount=amount)
        
        if cart_item.amount > 0:
            cart_item.save()
        else:
            cart_item.delete()
            
        return HttpResponseRedirect(reverse('order:cart'))
    except:
        return HttpResponseRedirect(reverse('products:index')) #home

class IndexView(LoginRequiredMixin, generic.ListView):
    template_name = 'order/index.html'

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

@login_required
def order_detail(request, order_id):
    try:
        shipping_data_editable_status = [0]
        context = {}
        user = request.user

        try:
            order = Order.objects.get(id=order_id, user=user)
        except:
            context['error_message'] = '這不是您的訂單，或此訂單不存在。'
            return render(request, 'order/detail.html', context)
        
        context['order'] = order
        if order.status in shipping_data_editable_status:
            context['shipping_data_editable'] = True
        if order.status == 1 and order.payment == 0:
            context['remittance_account_editable'] = True
        # context['message'] = '這不是您的訂單，或此訂單不存在。'
        return render(request, 'order/detail.html', context)
    except:
        return HttpResponseRedirect(reverse('products:index')) #home

@login_required
def order_create(request):
    # try:
    user = request.user
    cart_items = user.cartitem_set.all()
    shipping_fee = 60

    if cart_items:
        for cart_item in cart_items:
            if not cart_item.is_valid():
                return HttpResponseRedirect(reverse('order:cart'))

        user_name = user.last_name + ' ' + user.first_name
        user_name = '' if user_name == ' ' else user_name

        order = Order(
            user=user, 
            user_name=user_name,
            user_gender=user.userprofile.gender,
            user_contact_phone_no=user.userprofile.contact_phone_no,
            shipping_postal_code=user.userprofile.shipping_postal_code,
            shipping_address=user.userprofile.shipping_address,
            shipping_fee=shipping_fee,
            total_amount=0,
            status=0,
            payment=0,
            is_canceled=False)
        order.save()
        
        for cart_item in cart_items:
            order_item = OrderItem(
                order=order,
                item_name=cart_item.product.name,
                unit_price=cart_item.product.unit_price,
                amount=cart_item.amount,
                product=cart_item.product
            )
            order_item.save()
            cart_item.product.inventory_quantity -= order_item.amount
            cart_item.product.save()
            order.total_amount += order_item.unit_price * order_item.amount if order_item.amount > 0 else 0

        for cart_item in cart_items:
            cart_item.delete()

        order.total_amount += shipping_fee if shipping_fee > 0 else 0
        order.save()
        return HttpResponseRedirect(reverse('order:detail', args=[order.id]))
    else:
        return HttpResponseRedirect(reverse('products:index')) #home
    # except:
    #     return HttpResponseRedirect(reverse('products:index')) #home

@login_required
def next_step(request):
    #try:
    user = request.user
    order_id = int(request.POST.get('order_id', 0))
    order = None

    try:
        order = Order.objects.get(id=order_id, user=user)
    except:
        return HttpResponseRedirect(reverse('order:detail', args=[order_id]))

    status = order.status
    if status == 0:
        return order_confirm(request)

    return HttpResponseRedirect(reverse('order:detail', args=[order_id]))
    #except:


@login_required
def order_confirm(request):
    # try:
    shipping_data_editable_status = [0]
    user = request.user
    order_id = int(request.POST.get('order_id', 0))
    order = None

    try:
        order = Order.objects.get(id=order_id, user=user)
    except:
        return HttpResponseRedirect(reverse('order:detail', args=[order_id]))
    
    user_name = request.POST.get('user_name', '')
    user_gender = request.POST.get('user_gender', 0)
    user_contact_phone_no = request.POST.get('user_contact_phone_no', '')
    shipping_postal_code = request.POST.get('shipping_postal_code', '')
    shipping_address = request.POST.get('shipping_address', '')

    if user_name == '' or user_contact_phone_no == '' or shipping_postal_code == '' or shipping_address == '' or order.status not in shipping_data_editable_status:
        return HttpResponseRedirect(reverse('order:detail', args=[order_id]))

    order.user_name = user_name
    order.user_gender = user_gender
    order.user_contact_phone_no = user_contact_phone_no
    order.shipping_postal_code = shipping_postal_code
    order.shipping_address = shipping_address
    order.status = 1
    order.save()

    return HttpResponseRedirect(reverse('order:detail', args=[order_id]))

    # except:
    #     return HttpRes

class EditRemittanceAccount(LoginRequiredMixin, generic.UpdateView):
    model = Order
    template_name = 'order/remittance_account_update_form.html'
    fields = ['remittance_account']

    def get_context_data(self, **kwargs):
        context = super(EditRemittanceAccount, self).get_context_data(**kwargs)
        order = self.object
        if order.user != self.request.user or order.status != 1:
            raise Http404
        return context
        
    def get_success_url(self):
        return reverse('order:detail', args=[self.object.id])