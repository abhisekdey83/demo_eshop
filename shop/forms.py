from shop.models import Category, Product
from django import forms
class CatagoryForm(forms.ModelForm):
	class Meta:
		model=Category
		fields=['cat_name','cat_desc']

class ProductForm(forms.ModelForm):
	class Meta:
		model=Product
		fields="__all__"