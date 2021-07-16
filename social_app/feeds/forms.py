from django import forms
from django.forms import models
from .models import Post

class PostForm(forms.ModelForm):
    
    class Meta:
        model=Post
        fields= ['image','text']