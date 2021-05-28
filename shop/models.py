from django.db import models

# Create your models here.

class Category(models.Model):
	cat_id = models.AutoField(primary_key=True)
	cat_name = models.CharField(max_length=255)
	cat_desc = models.CharField(max_length=255)
		






class Product(models.Model):
	STATUS_CHOICES = (
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
    )
	DEFAULT_CHOICES = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )
	item_id = models.AutoField(primary_key=True)
	cat_id = models.ForeignKey(Category, on_delete=models.CASCADE,null=True,blank=True)
	name = models.CharField(max_length=255)
	sku = models.TextField(max_length=255)
	description = models.TextField(null=True,blank = True)
	status=models.CharField(max_length=100,choices=STATUS_CHOICES,null=True,blank=True)
	barcode = models.TextField(max_length=255,null=True,blank=True)
	features = models.TextField(null=True,blank = True)
	meta_title = models.CharField(max_length=255,null=True,blank = True)
	meta_tag = models.CharField(max_length=255,null=True,blank = True)
	meta_keyword = models.TextField(null=True,blank = True)
	meta_description = models.TextField(null=True,blank = True)
	image = models.ImageField(upload_to='images/')
	alt = models.CharField(max_length=255)
	is_shipped_to_home = models.CharField(max_length=100,choices=DEFAULT_CHOICES,null=True,blank=True)