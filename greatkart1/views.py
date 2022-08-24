from django.shortcuts import render
from store.models import Product
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    products=Product.objects.all().filter(is_available=True)
    paginator=Paginator(products,3)
    page=request.GET.get('page')
    paged_product=paginator.get_page(page)
    return render(request,'index.html',{'Product':paged_product})
