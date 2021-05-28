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
    Category = Category.objects.all()  
    return render(request,"show.html",{'Category':Category})



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











