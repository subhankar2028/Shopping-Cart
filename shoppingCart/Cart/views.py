from django.shortcuts import render
from django.http import  HttpResponse
from django.contrib.sessions.models import Session
from django.contrib.auth import authenticate
from django.contrib.auth import logout
from datetime import *
from . models import *
import json
# from django.http import JsonResponse
from django.db.models import Sum

def home(request):
    if request.session.has_key('is_logged'):
        # user=UserProfile.objects.get(user=User.objects.get(username=request.session['username']))
        # print(user.profile_image)
        products = Product.objects.all()    
        # productImage=products.productImage	
        username=request.session['username']
        user_id = User.objects.get(username = request.session['username']).id
        productInCart = Cart.objects.all().filter(user_id = user_id, checkOut = False)  
        context={
            'products'          :   products,
            # 'productImage'      :   productImage,
            'username'          :   username,
            'count_cart_list'   :   productInCart.count(),            }
        return render(request, 'index.html', context=context)
    else:
        return login(request)
				

def login(request):
    if request.method == 'GET':
        if request.session.has_key('is_logged'):
            return home(request)
        else:
            return render(request, 'login.html', context={})
    else:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            user.last_login = datetime.today()
            user.save()
            request.session['is_logged'] = True
            request.session['username'] = username
            print("Signin successfull and is_logged value is : {}".format(request.session.has_key('is_logged')))
            return home(request)
        else:
            context = {"is_SigninFailed": "Sign in failed."}
            return render(request, 'login.html', context={})


def logout(request):
#     logout(request)
#     return login(request)
    if request.session.has_key('is_logged'):
        del request.session['is_logged']   
        del request.session['username']     
        return login(request)
    else:
        return login(request)



def ajaxReq(request):
    user_id = User.objects.get(username = request.session['username']).id
    product_id = request.GET['product_id']
    product = Product.objects.get(id = product_id)
    cart = Cart(user_id = user_id, product_id = product_id, productCoast = product.productCoast,)
    cart.save()
    productInCart = Cart.objects.all().filter(user_id = user_id, checkOut = False)  
    context = {
        'count_cart_list': productInCart.count(),
        }
    return HttpResponse(json.dumps(context), content_type="application/json")


def checkout(request):
    productList = []
    user_id = User.objects.get(username = request.session['username']).id
    productInCart = Cart.objects.all().filter(user_id = user_id, checkOut = False)
    total = 0
    for product in productInCart:
        print(product.productCoast)
        total = total + int(product.productCoast)

    request.session['cartTotal'] = total
    context={
        'productInCart' : productInCart,
        'total'         : total,
        }
    return render(request, 'checkoutTable.html', context = context)


def applyCoupon(request):
    code = request.POST['coupon']
    total = float(request.POST['total'])
    percentage = Coupon.objects.get(code = code).discount
    after_deduction = total-((percentage/100)*total)
    request.session['cartTotal'] = after_deduction
    # print(request.session['cartTotal'])
    context = {
        'after_deduction' : 'Coupon applied succesfully. Total Cost : ' + str(after_deduction),
        }
    return HttpResponse(json.dumps(context), content_type="application/json")

def proceedCheckout(request):
    print(request.session['cartTotal'])
    if request.session['cartTotal'] == 0:
        return HttpResponse("Empty Cart")
    user = User.objects.get(username = request.session['username'])
    user_profile = UserProfile.objects.get(user_id = user.id)
    userName = str(user.first_name) + str(user.last_name)
    address = user_profile.address
    productInCart = Cart.objects.all().filter(user_id = user.id, checkOut = False)
    for product in productInCart:
        product.checkOut = True
        product.save()
    context = {
        'userName'  :  userName,
        'address'   :   address,
        'total'     :   request.session['cartTotal'],
    }
    request.session['cartTotal'] = 0
    return render(request, 'proceedCheckout.html', context = context)