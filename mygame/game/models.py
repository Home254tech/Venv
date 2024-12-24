from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.

class Profile(models.Model):
    user=models.ForeignKey(User, on_delete= models.CASCADE)
    image= models.ImageField(default= 'dafault.png', upload_to='user_pics')
    # created_on= models.DateTimeField(auto_now_add= True)

class Post(models.Model): 
    title = models.CharField(max_length=200) 
    content = models.TextField() 
    author = models.ForeignKey(User, on_delete=models.CASCADE) 
    pub_date = models.DateTimeField(auto_now_add=True) 

    def __str__(self): 
        return self.title 

    class Meta: 
        ordering = ['-pub_date']