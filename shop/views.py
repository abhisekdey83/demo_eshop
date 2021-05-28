from django.http import HttpResponse
from django.shortcuts import render, redirect  
from shop.forms import CatagoryForm  
from shop.models import Category  

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
    Category = Category.objects.get(id=id)  
    return render(request,'edit.html', {'Category':Category})




def updatecat(request, id):  
    Category = Category.objects.get(id=id)  
    form = CatagoryForm(request.POST, instance = Category)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'Category': Category})


def destroycat(request, id):  
    Category = Category.objects.get(id=id)  
    Category.delete()  
    return redirect("/show")  





#product operation


def ProductSave(request):
	if request.method == "POST":  
		form = ProductForm(request.POST)  
		if form.is_valid():  
			try:  
				form.save()  
				return redirect('/show_Product')  
			except:  
				pass
			else:  
				p_form = ProductForm()
				

	return render(request,'home.html',{'p_form':p_form})
	 


def show_Product(request):  
    Product = Product.objects.all()  
    return render(request,"show.html",{'Product':Product})



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










