from django.shortcuts import render, redirect
from . models import Product

def index(request):
    products = Product.objects.all()
    context = {'product':products}
    return render(request, 'product_app/index.html', context)

def create(request):
    print(request.POST)
    product_app = Product(name=request.POST['name'],description=request.POST['description'])
    product_app.save()
    return redirect('/')