from django.urls import path
from . import views
urlpatterns = [

path('',views.home, name='home'),
path('CategorySave', views.CategorySave),  
path('show_cat',views.show_cat),  
path('editcat/<int:id>', views.editcat),  
path('updatecat/<int:id>', views.updatecat),  
path('destroycat/<int:id>', views.destroycat),  

]