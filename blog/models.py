from django.db import models
from datetime import date

from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    category_name = models.CharField('Category Name',max_length=255)
    category_status = models.IntegerField('Category Status',default=1,max_length=255)
    created_at = models.DateField(default=date.today)

    class Meta:
        db_table = 'categories'



class Blog(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    blog_title = models.CharField('Blog Title',max_length=255)
    blog_description = models.TextField('Blog Description')
    blog_featured_image = models.ImageField(upload_to='images/', max_length=255)
    status = models.IntegerField(max_length=10,default=1)
    blog_posted_date = models.DateField(default=date.today)


    class Meta:
        db_table = 'blogs'


