from django.shortcuts import render, redirect
from .models import Product


def index(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'product_app/index.html', context)


def create(request):
    print(request.POST)
    product_app = Product(name=request.POST['name'], description=request.POST['description'])
    product_app.save()
    return redirect('/')


def edit(request, id):
    product = Product.objects.get(id=id)
    context = {'product': product}
    return render(request, 'product_app/edit.html', context)

def update(request, id):
    product = Product.objects.get(id=id)
    product.name = request.POST['name']
    product.description = request.POST['description']
    product.save()
    return redirect('/')


