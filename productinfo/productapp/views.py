from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

# Create your views here.
def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')
def product_list(request):
    products=Product.objects.all()
    print(products)

    return render(request,'productlist.html',{'products':products})
