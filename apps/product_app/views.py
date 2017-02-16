from django.shortcuts import render, redirect
from .models import Product, Category


def index(request):
    products = Product.objects.all()
    category = Category.objects.all()
    context = {'products': products, 'category': category}

    return render(request, 'product_app/index.html', context)


def create(request):
    category_instance = Category.objects.get(pk=request.POST['category'])
    product_app = Product(name=request.POST['name'], description=request.POST['description'], category=category_instance)
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

def destroy(request, id):
    product = Product.objects.get(id=id)
    product.delete()
    return redirect('/')