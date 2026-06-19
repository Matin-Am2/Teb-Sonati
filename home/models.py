from django.db import models
from django.utils.text import slugify
import re

# Create your models here.


# def slugify_fa(text):
#     text = re.sub(r'[^\u0600-\u06FF\s]', '', text)
#     text = slugify(text,allow_unicode=True)    

#     return text

class Product(models.Model):
    category = models.ForeignKey("Category",on_delete=models.SET_NULL,related_name="products",null=True,blank=True,verbose_name="دسته بندی")
    name = models.CharField(max_length=255,verbose_name="نام محصول")
    slug = models.SlugField(unique=True,verbose_name="اسلاگ",allow_unicode=True,blank=True)
    image = models.ImageField(upload_to="products/",verbose_name="عکس")
    history = models.TextField(null=True,blank=True,verbose_name="تاریخچه")
    benefits = models.TextField(null=True,blank=True,verbose_name="فواید")
    usage = models.TextField(null=True,blank=True,verbose_name="طریقه مصرف")
    precautions = models.TextField(null=True,blank=True,verbose_name="موارد احتیاط")
    created_at = models.DateTimeField(auto_now=True,null=True)
    updated_at = models.DateTimeField(auto_now_add=True,null=True)

    # def save(self,*args,**kwargs):
    #     if not self.slug:
    #         self.slug = slugify_fa(self.name)
    #     return super().save(*args,**kwargs)

    def __str__(self):
        return self.name

class Category(models.Model): 
    name = models.CharField(max_length=255,verbose_name="نام دسته بندی")
    slug = models.SlugField(unique=True,verbose_name="اسلاگ",allow_unicode=True)
    
    def __str__(self):
        return self.name
    
    # def save(self,*args,**kwargs):
    #     if not self.slug:
    #         self.slug = slugify_fa(self.name,allow_unicode=True)
    #     return super().save(*args,**kwargs)
    
    class Meta:
        verbose_name = 'category'
        verbose_name_plural = "categories"

