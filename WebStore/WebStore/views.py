from django.http import HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.utils import timezone
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from administration.models import Configuration, UserProfile
from .forms import CustomerCreateForm, CustomerUpdateForm, CustomerPasswordUpdateForm

def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('products:index')) #home

def customer_login(request):
    # try:
    if request.method == 'GET':
        if request.user.is_authenticated:
            return HttpResponseRedirect(request.GET.get('next', reverse('products:index'))) #home
        return render(request, 'auth/customer_login.html')
    elif request.method == 'POST':
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is not None and user.is_active and not user.is_staff:
            login(request, user)
            return HttpResponseRedirect(request.GET.get('next', reverse('products:index'))) #home
        else:
            context = {}
            context['error_message'] = '您輸入的電子郵件信箱或密碼有誤，或是您尚未建立帳號！'
            return render(request, 'auth/customer_login.html', context)
    # except:
    #     context = {}
    #     context
    #     return render(request, 'userprofile/login-page.html', context)

def customer_create(request):
    # try:
    context = {}
    if request.method == 'GET':
        context['form'] = CustomerCreateForm()
        return render(request, 'auth/customer_form.html', context)
    elif request.method == 'POST':
        context['username'] = request.POST['username']
        password = request.POST['password']
        password_confirm = request.POST['password_confirm']
        context['last_name'] = request.POST['last_name']
        context['first_name'] = request.POST['first_name']
        context['gender'] = int(request.POST['gender'])
        context['shipping_postal_code'] = request.POST['shipping_postal_code']
        context['shipping_address'] = request.POST['shipping_address']
        context['contact_phone_no'] = request.POST['contact_phone_no']

        if password != password_confirm:
            context['form'] = CustomerCreateForm(initial=context)
            context['error_message'] = '您輸入的密碼和確認密碼不一致！'
            return render(request, 'auth/customer_form.html', context)

        if User.objects.filter(username=context['username']).count() != 0:
            context['form'] = CustomerCreateForm(initial=context)
            context['error_message'] = '這個帳號已存在！'
            return render(request, 'auth/customer_form.html', context)

        user = User.objects.create_user(
            username=context['username'],
            email=context['username'],
            password=password
        )
        user.last_name = context['last_name']
        user.first_name = context['first_name']
        user.is_active = True
        user.save()
        userprofile = UserProfile(
            user=user,
            gender=context['gender'],
            shipping_postal_code=context['shipping_postal_code'],
            shipping_address=context['shipping_address'],
            contact_phone_no=context['contact_phone_no'],
        )
        userprofile.save()
        
        user = authenticate(request, username=context['username'], password=password)
        login(request, user)
        return HttpResponseRedirect(request.GET.get('next', reverse('products:index'))) #home

    # except:
    #     context = {}
    #     context
    #     return render(request, 'userprofile/login-page.html', context)

@login_required
def profile(request):
    return render(request, 'auth/profile.html')

@login_required
def profile_update(request):
    context = {}
    if request.method == 'GET':
        originals = {}
        originals['last_name'] = request.user.last_name
        originals['first_name'] = request.user.first_name
        originals['gender'] = request.user.userprofile.gender
        originals['shipping_postal_code'] = request.user.userprofile.shipping_postal_code
        originals['shipping_address'] = request.user.userprofile.shipping_address
        originals['contact_phone_no'] = request.user.userprofile.contact_phone_no
        context['form'] = CustomerUpdateForm(initial=originals)
        return render(request, 'auth/profile_form.html', context)
    elif request.method == 'POST':
        request.user.last_name = request.POST.get('last_name', request.user.last_name)
        request.user.first_name = request.POST.get('first_name', request.user.first_name)
        request.user.userprofile.gender = request.POST.get('gender', request.user.userprofile.gender)
        request.user.userprofile.shipping_postal_code = request.POST.get('shipping_postal_code', request.user.userprofile.shipping_postal_code)
        request.user.userprofile.shipping_address = request.POST.get('shipping_address', request.user.userprofile.shipping_address)
        request.user.userprofile.contact_phone_no = request.POST.get('contact_phone_no', request.user.userprofile.contact_phone_no)
        request.user.userprofile.save()
        request.user.save()
        return HttpResponseRedirect(reverse('profile'))

@login_required
def password_update(request):
    context = {}
    if request.method == 'GET':
        context['form'] = CustomerPasswordUpdateForm()
        return render(request, 'auth/password_form.html', context)
    elif request.method == 'POST':
        username = request.POST['username']
        old_password = request.POST['old_password']
        password = request.POST['password']
        password_confirm = request.POST['password_confirm']

        if username != request.user.username:
            context['error_message'] = '請輸入您正確的電子郵件信箱！'
        elif password != password_confirm:
            context['error_message'] = '您輸入的密碼和確認密碼不一致！'
        else:
            user = authenticate(request, username=username, password=old_password)
            if user is not None and user.is_active and not user.is_staff:
                user.set_password(password)
                user.save()
                return HttpResponseRedirect(reverse('profile'))
            context['error_message'] = '您輸入的舊密碼有誤！'

        context['form'] = CustomerPasswordUpdateForm()
        return render(request, 'auth/password_form.html', context)
        
        
