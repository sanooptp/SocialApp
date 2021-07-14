from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(User, verbose_name= 'username', on_delete=models.CASCADE)
    text = models.TextField(max_length=100)
    image = models.ImageField( upload_to=None, height_field=None, width_field=None, max_length=None)
    
    def __str__(self):
        return self.id
        