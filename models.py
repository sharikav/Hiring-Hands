from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    
    is_customer = models.BooleanField(default=False)
    is_labourer = models.BooleanField(default=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=10)
    locality = models.CharField(max_length=200)
    photo = models.ImageField(upload_to="images/", height_field=None, width_field=None, max_length=100)


      
 
class Customer(models.Model):
    user= models.OneToOneField(User , on_delete= models.CASCADE, primary_key= True)
    email = models.EmailField(max_length=254)

class Labourer(models.Model):
    user= models.OneToOneField(User , on_delete= models.CASCADE, primary_key= True)
    skill_set= models.CharField(max_length=100)

class Interface(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    labourer = models.ForeignKey(Labourer, on_delete=models.CASCADE)
    details = models.CharField(max_length=200)




