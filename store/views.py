from django.shortcuts import render,get_object_or_404
from store.models import Product
from category.models import category

# Create your views here.
def store(request,category_slug=None):
    if(category_slug !=None):
        categories=get_object_or_404(category,slug=category_slug)
        products=Product.objects.filter(category=categories,is_available=True)
        product_count=products.count()
    else:
        products=Product.objects.all().filter(is_available=True)
        product_count=products.count()
    return render (request,'store.html',{'products':products,'pcount':product_count})

def product_detail(request,category_slug,product_slug):
    single_product=Product.objects.get(category__slug=category_slug,slug=product_slug)
    return render(request,'product_details.html',{'sproduct':single_product})