from django.db import models
from django.contrib.auth.models import User
from django.db.models import aggregates


GENDER_MALE = 'Male'
GENDER_FEMALE = 'Female'
GENDER_OTHERS = 'Others'
GENDER_CHOICE = (
    (GENDER_MALE,'Male'),
    (GENDER_FEMALE,'Female'),
    (GENDER_OTHERS,'Others'),
)
class UserDetail(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField(verbose_name='Age')
    gender = models.CharField( max_length=20, choices= GENDER_CHOICE)
    occupation = models.IntegerField(verbose_name='Occupation')

    def __str__(self):
        return self.user.username
    
# comment for testing