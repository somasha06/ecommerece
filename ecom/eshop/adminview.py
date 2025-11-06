from django.shortcuts import render,redirect
from .adminform import Categoryform,Productform
from .models import Product,Category
from django.shortcuts import get_object_or_404
from django.contrib import messages

def admindashboard(r):
    count={}
    
    return render(r,"admin/dashboard.html")

def managecategories(r):
    form=Categoryform(r.POST or None) # categoryform connects form field to database model
    categories=Category.objects.all()
    if r.method == "POST": #user clicked submit
        if form.is_valid(): #check required feild
            form.save() # return all data to the table whatever we fill in insert form
            return redirect(managecategories)
    return render(r,"admin/managecategories.html",{"form":form,"categories":categories})

def deletecategory(r,id):
    deletedcategory=Category.objects.get(id=id)
    deletedcategory.delete()
    return redirect(managecategories)

# def viewcategory(r,id):
#     category=Category.objects.get(id=id)
#     return render(r,"admin/viewcategory.html",{"category":category})

def insertproduct(r):
    form=Productform(r.POST or None,r.FILES or None )

    if r.method == "POST":
        if form.is_valid():
            form.save()
            return redirect(manageproduct)
    return render(r,"admin/insertproduct.html",{"form":form})

def manageproduct(r):
    products=Product.objects.all()
    return render(r,"admin/manageproduct.html",{"products":products})

def deleteproduct(r,id):
    obj=Product.objects.get(id=id)
    obj.delete()
    return redirect(manageproduct)

# def viewproduct(r,id):
#     product=Product.objects.get(id=id)
#     return render(r,"admin/viewproduct.html",{"product":product})
    
def editproduct(r,id):
    product=Product.objects.get(id=id)
    form=Productform(r.POST or None,r.FILES or None,instance=product)
    if r.method=="POST":
        form.is_valid()
        form.save()
        return redirect(manageproduct)
    return render(r,"admin/editproduct.html",{"form":form})   