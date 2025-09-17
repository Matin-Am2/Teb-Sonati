from django.db import models
from django.utils.text import slugify
import re

# Create your models here.


def slugify_fa(text):
    text = re.sub(r'[^\u0600-\u06FF\s]', '', text)
    text = slugify(text,allow_unicode=True)    

    return text

class Product(models.Model):
    category = models.ForeignKey("Category",on_delete=models.SET_NULL,related_name="products",null=True,blank=True,verbose_name="دسته بندی")
    name = models.CharField(max_length=255,verbose_name="نام محصول")
    slug = models.SlugField(unique=True,verbose_name="اسلاگ",allow_unicode=True,blank=True)
    description = models.TextField(verbose_name="توضیحات")
    image = models.ImageField(upload_to="products/",verbose_name="عکس")
    extra_info = models.JSONField(null=True,blank=True,verbose_name="اطلاعات اضافی")


    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify_fa(self.name)
        return super().save(*args,**kwargs)

    def __str__(self):
        return self.name

class Category(models.Model): 
    name = models.CharField(max_length=255,verbose_name="نام دسته بندی")
    slug = models.SlugField(unique=True,verbose_name="اسلاگ",allow_unicode=True)
    
    def __str__(self):
        return self.name
    
    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify_fa(self.name,allow_unicode=True)
        return super().save(*args,**kwargs)
    
    class Meta:
        verbose_name = 'category'
        verbose_name_plural = "categories"

class Article(models.Model):
    title = models.CharField(max_length=200,verbose_name="عنوان")
    slug = models.SlugField(unique=True,verbose_name="اسلاگ")
    content = models.TextField(verbose_name="محتوا")
    image = models.ImageField(upload_to="articles/", blank=True, null=True,verbose_name="عکس")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True,verbose_name="دسته بندی")
    created_at = models.DateTimeField(auto_now_add=True,verbose_name="زمان ایجاد شده")

    def __str__(self):
        return self.name