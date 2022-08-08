from django.db import models
from django.urls import reverse

# Create your models here.

class category(models.Model):
    category_name=models.CharField(max_length=200,unique=True)
    slug=models.CharField(max_length=200,unique=True)
    description=models.TextField(max_length=255)
    images=models.ImageField(upload_to='images/category')

    class Meta:
        verbose_name='categorys'
        verbose_name_plural='categories'

    def __str__(self):
        return self.category_name

    def get_url(self):
        return reverse('category_product',args=[self.slug])