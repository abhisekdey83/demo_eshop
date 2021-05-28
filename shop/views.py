from django.http import HttpResponse
from django.shortcuts import render, redirect  
from shop.forms import CatagoryForm , ProductForm
from shop.models import Category, Product 
import pdb

# Create your views here.

def home(request):
	return render(request,'home.html')



def CategorySave(request):
	if request.method == "POST":  
	    form = CatagoryForm(request.POST)  
	    if form.is_valid():  
	        try:  
	            form.save()  
	            return redirect('/show_cat')  
	        except:  
	            pass  
	else:  
	    form = CatagoryForm()  
	return render(request,'home.html',{'form':form})
	 


def show_cat(request):  
    Categorys = Category.objects.all()  
    return render(request,"show.html",{'Categorys':Categorys})



def editcat(request, id):  
	Category = Category.objects.get(id=cat_id)  
	return render(request,'edit.html', {'Category':Category})




def updatecat(request, id):  
    Category = Category.objects.get(id=id)  
    form = CatagoryForm(request.POST, instance = Category)  
    if form.is_valid():  
        form.save()  
        return redirect("/show_cat")  
    return render(request, 'edit.html', {'Category': Category})


def destroycat(request, id):  
    Category = Category.objects.get(id=cat_id)  
    Category.delete()  
    return redirect("/show_cat")  





#product operation


def ProductSave(request):

	if request.method == "POST":  
	    pform = ProductForm(request.POST)  
	    if pform.is_valid():  
	        try:  
	            pform.save()  
	            return redirect('/show_Product')  
	        except:  
	            pass  
	else:  
	    pform = ProductForm()  
	return render(request,'product_add.html',{'pform':pform})
	 


def show_Product(request):  
    Products = Product.objects.all()  
    return render(request,"product_show.html",{'Products':Products})



def editProduct(request, id):  
    Product = Product.objects.get(id=id)  
    return render(request,'edit.html', {'Product':Product})




def updateProduct(request, id):  
    Product = Product.objects.get(id=id)  
    form = ProductForm(request.POST, instance = Product)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'Product': Product})


def destroyProduct(request, id):  
    Product = Product.objects.get(id=id)  
    Product.delete()  
    return redirect("/show")










