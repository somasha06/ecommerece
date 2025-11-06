from django.shortcuts import render
from .models import Category,Product

def home(r):
    data={}
    data["categories"]=Category.objects.all()
    data["products"]=Product.objects.all()
    return render(r,"home.html",data)
