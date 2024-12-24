from django import forms
from . import models
from django.contrib.auth.forms import AuthenticationForm



#my forms will be here

class Profileform(forms.ModelForm):    
    class Meta:
        model= models.Profile
        fields = ("__all__")



class Postform(forms.ModelForm):    
    class Meta:
        model = models.Post
        fields = ("__all__")
