from django.shortcuts import render
from rest_framework.response import Response
from django.contrib.auth import logout as django_logout
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.db.models import Sum
import random
from .models import Products, Temp

# Create your views here.
# def Home(request):
#     return render(request, "home.html", {})

def Home(request):
    
    products = Products.objects.all()
   
    searchQuiry = request.GET.get("search")

    if searchQuiry:
        found = Products.objects.get(title=searchQuiry)
        if found:
            products = found
        else:
            return Response(status.HTTP_404_NOT_FOUND)

    print(request.method)

    allProducts = {
        'products': products
    }   
    
    return render(request, 'home.html', allProducts)

def delete(request):
    Temp.objects.all().delete()
    messages.success(request, f"Than you for choosing Bobs, your order has been successfuly created!!")
    return HttpResponseRedirect("../home")

    
def About(request):
    return render(request, 'about.html', {})

def Buy(request, id):
    product = Products.objects.get(id=id)
    categ = Products.objects.filter(category=product.category).exclude(title=product.title)

    purchase = {
        "product": product,
        "category": categ
    }
    print(purchase)
    return render(request, 'buy.html', purchase)


def cart(request, id):
    product = Products.objects.get(id=id)
    quantity = request.GET["qty"]
    price = product.price
    original_id = product.id
    current = price * int(quantity)
    # num = random.randrange
    Temp.objects.create(title=product.title, price=product.price, quantity=quantity, current_total=current)
    # print(num)
    cart_products = Temp.objects.all()
    final_total = Temp.objects.aggregate(total_price=Sum("current_total"))


    context = {
        "products": cart_products,
        "current_total": current,
        "final_total": final_total["total_price"],
        "original_id": original_id,
    }
    

    return render(request, 'cart.html', context)

def SignUp(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Hi {username}, your aaccount was successfuly created")
            return HttpResponseRedirect("../")
        else:
            messages.success(request, f"Account not successfuly created, recheck your details")
            form = UserCreationForm()

    form = UserCreationForm
    context={
        "form": form
    }
    return render(request, 'sign_up.html', context)

def logout(request):
    django_logout(request)
    return HttpResponseRedirect("../")

def Search(request):
    if request.method == "GET":
        queryStr = request.GET.get('query')

        if queryStr:
            found = Products.objects.filter(title__icontains=queryStr)
            results = {
                "product": found
            }
            return render(request, 'search.html', results)
        else:
            return render(request, 'search.html', {})





