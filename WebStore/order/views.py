from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse


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
    return render(request, 'order/cart.html', context)

@login_required
def cart_item_edit(request, product_id=0):
    try:
        user = request.user
        product = Product.objects.get(id=int(request.POST.get('product', product_id)))
        amount = int(request.POST.get('amount', 1))
        item = None

        try:
            item = user.cartitem_set.get(product=product)
            item.amount += amount
        except:
            item = CartItem(user=user, product=product, amount=amount)
        
        if item.amount > 0:
            item.save()
        else:
            item.delete()
        return HttpResponseRedirect(reverse('order:cart'))
    except:
        return HttpResponseRedirect(reverse('products:index')) #home

@login_required
def order_create(request):
    # try:
    user = request.user
    cart_items = user.cartitem_set.all()
    if cart_items:
        order = Order(
            user=user, 
            user_name=user.last_name + ' ' + user.first_name,
            shipping_address=user.userprofile.shipping_address,
            shipping_fee=60,
            total_amount=101,
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
    return HttpResponseRedirect(reverse('order:cart'))
    # except:
    #     return HttpResponseRedirect(reverse('products:index')) #home