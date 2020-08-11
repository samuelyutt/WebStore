from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse


from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User

from products.models import Product
from .models import CartItem


# Create your views here.
@login_required
def cart(request):
    context = {}
    context['cart_items'] = request.user.cartitem_set.all()
    return render(request, 'order/cart.html', context)

@login_required
def add_to_cart(request):
    user = request.user
    add_product = Product.objects.get(id=int(request.POST['add_product']))
    add_amount = int(request.POST['add_amount'])
    
    print(add_product)
    print(add_product.name)
    print(add_amount)

    try:
        item = user.cartitem_set.get(product=add_product)
        item.amount += add_amount
        item.save()
    except:
        new_item = CartItem(user=user, product=add_product, amount=add_amount)
        new_item.save()

    context = {}
    context['cart_items'] = user.cartitem_set.all()
    return HttpResponseRedirect(reverse('order:cart'))