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
def edit_cart_item(request):
    user = request.user
    product = Product.objects.get(id=int(request.POST['product']))
    amount = int(request.POST['amount'])
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

    context = {}
    context['cart_items'] = user.cartitem_set.all()
    return HttpResponseRedirect(reverse('order:cart'))