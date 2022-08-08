from ssl import create_default_context
from django.db import models
from category.models import category
from django.urls import reverse

# Create your models here.
class Product(models.Model):
    product_name=models.CharField(max_length=200,unique=True)
    slug        =models.SlugField(max_length=200,unique=True)
    description=models.TextField(max_length=255)
    quantity    =models.IntegerField()
    category    =models.ForeignKey(category,on_delete=models.CASCADE)
    image       =models.ImageField(upload_to='photos/product')
    price       =models.IntegerField()
    stock       =models.IntegerField()
    is_available=models.BooleanField(default=True)
    created_data=models.DateTimeField(auto_now=True)
    modified_data=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product_name
        
    def get_url(self):
        return reverse('product_details',args=[self.category.slug,self.slug])
