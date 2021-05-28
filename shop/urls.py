from django.urls import path
from . import views
urlpatterns = [

#category urls
path('',views.home, name='home'),
path('CategorySave', views.CategorySave),  
path('show_cat',views.show_cat),  
path('editcat/<int:id>', views.editcat),  
path('updatecat/<int:id>', views.updatecat),  
path('destroycat/<int:id>', views.destroycat),

#product urls

path('ProductSave', views.CategorySave),  
path('show_Product',views.show_cat),  
path('editProduct/<int:id>', views.editcat),  
path('updateProduct/<int:id>', views.updatecat),  
path('destroyProduct/<int:id>', views.destroycat),

]