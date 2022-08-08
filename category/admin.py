from django.contrib import admin
from.models import category

# Register your models here.
class Admincategory(admin.ModelAdmin):
    prepopulated_fields={'slug':('category_name',)}

admin.site.register(category,Admincategory)