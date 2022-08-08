from django.contrib import admin
from .models import Product

# Register your models here.
class AdminProduct(admin.ModelAdmin):
    prepopulated_fields ={'slug':('product_name',)}
    list_display =('product_name','slug','description','quantity','category','price','stock','is_available',)
    
admin.site.register(Product,AdminProduct)
