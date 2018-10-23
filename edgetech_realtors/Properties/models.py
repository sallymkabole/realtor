from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Letter(models.Model):
    name =models.CharField(max_length=30, primary_key=True, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField(max_length=400)
class Property(models.Model):
    name =models.CharField(max_length=130, primary_key=True,unique=True)
    description = models.TextField(max_length=400)
    location =models.CharField(max_length=30)
    #created_at = models.DateTimeField(auto_now_add=True)

    image = models.CharField (max_length=30, unique=True)
    #user = models.ForeignKey(User,null=False, on_delete=models.CASCADE)
    status = models.BooleanField(default=False, null=False)
    price = models.DecimalField(max_digits=10,decimal_places=2, null=False)

    def __str(self):
            return self.name

class Role(models.Model):
    name =models.CharField(max_length=130, primary_key=True,unique=True,  null=False)
    created_at = models.DateTimeField(auto_now_add=True)


class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=30)
    password = models.CharField(max_length=50)
    status = models.ForeignKey(User,null=False, on_delete=models.CASCADE)
    created_at = created_at = models.DateTimeField(auto_now_add=True,)
