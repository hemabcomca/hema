from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse

# Dummy user credentials for simplicity
USERNAME = 'user'
PASSWORD = 'password'

# View for the login page
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username == USERNAME and password == PASSWORD:
            return redirect('/products')
        else:
            return HttpResponse("Invalid credentials", status=403)
    
    return render(request, 'shop/login.html')

# View for the product page
def products(request):
    return render(request, 'shop/product.html')

# View for logging out (Redirect to login page)
def logout(request):
    return redirect('/login')
from django.shortcuts import render
from .models import Product

def products(request):
    products = Product.objects.all()
    return render(request, 'shop/product.html', {'products': products})
def home(request):
    return render(request, 'shop/home.html')
