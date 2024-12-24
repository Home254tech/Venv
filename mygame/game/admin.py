from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.Post)
class Post(admin.ModelAdmin):
    list_display=['title', 'author', 'content', 'pub_date']
    list_filter=['author', 'pub_date']

@admin.register(models.Profile)
class ProfilePic(admin.ModelAdmin):
    list_display=['user', 'image',]



