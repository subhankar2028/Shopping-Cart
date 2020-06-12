from django.db import models
from django.contrib.auth.models import User
from datetime import *


USER_TYPE = (
    (1, "Admin"),
    (2, "User")
)
class UserProfile(models.Model):
    user            = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)   #This line binds this extended profile with user
    dob             = models.DateTimeField(auto_now=True)
    profile_image   = models.ImageField(upload_to="Cart/ProfileImage", blank=True, null=True)
    phone           = models.CharField(max_length=10, blank=True, null=True)
    usr_type        = models.IntegerField(choices=USER_TYPE, default=2)
    address         = models.TextField(max_length=500, blank=True, null=True)
    def __str__(self):
        return str(self.user)
    class Meta:
        db_table="UserProfile"

class Product(models.Model):
    name            = models.CharField(max_length = 50, blank = False, null = False)
    productImage    = models.ImageField(upload_to="Cart/productImage", blank=True, null=True)
    productCoast    = models.FloatField(blank=False, null=False)
    productDesc     = models.TextField(max_length=500, blank=True, null=True)
    def __str__(self):
        return str(self.name)
    class Meta:
        db_table="Product"


class Cart(models.Model):
    user        =   models.ForeignKey(User, on_delete=models.CASCADE)
    product     =   models.ForeignKey(Product, on_delete=models.CASCADE)
    productCoast= models.FloatField( blank=False, null=False)
    count       =   models.IntegerField(default=1)
    checkOut    =   models.BooleanField(default=False)
    def __str__(self):
        return str(self.user) + str(self.product)
    class Meta:
        db_table="Cart"

class Coupon(models.Model):
    code = models.CharField(null=False, blank=False, max_length=10)
    discount = models.FloatField(default=False, null=False, blank=False)
    def __str__(self):
        return str(self.discount) 
    class Meta:
        db_table="Coupon"
