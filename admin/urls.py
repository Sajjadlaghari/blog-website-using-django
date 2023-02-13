from django.contrib import admin
from django.urls import path, include
from admin import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('/home', views.adminHome, name="admin-home"),
    path('/form', views.adminForm, name="form"),
    path('/table', views.adminTable, name="table"),
    path('/logout', views.Logout, name='logout'),
    path('/add-new-blog', views.addBlog, name='add-new-blog'),
    path('/view-blogs', views.viewBlogs, name='view-blogs'),
    path('/blog-edit/<id>', views.editBlog, name='edit-blog'),
    path('/blog-status/<id>', views.ChangeBlogStatus, name='blog-status'),

    path('/update-blog', views.updateBlog, name='update-blog'),
    path('/delete-blog/<id>', views.deleteBlog, name='delete-blog'),

    # categories url

    path('/add-new-category', views.addCategory, name='add-new-category'),
    path('/view-all-categories', views.viewCategories, name='view-categories'),
    path('/view-inactive-categories', views.viewInActiveCategories, name='view-inactive-categories'),
    path('/category-edit/<id>', views.editCategory, name='category-edit'),
    path('/update-category', views.updateCategory, name='update-category'),
    path('/category-status/<id>', views.ChangeCategoryStatus, name='category-status'),
    path('/delete-category/<id>', views.deleteCategory, name='delete-category'),
]