from django.db import models


# Create your models here.
class contactdb(models.Model):
    Name = models.CharField(max_length=50, blank=True, null=True)
    Email = models.CharField(max_length=50, blank=True, null=True)
    Phone = models.IntegerField(blank=True, null=True)
    Subject = models.CharField(max_length=50, blank=True, null=True)
    Message = models.CharField(max_length=100, blank=True, null=True)


class logindb(models.Model):
    Uname = models.CharField(max_length=50, blank=True, null=True)
    Emailid = models.CharField(max_length=50, blank=True, null=True)
    Passw = models.CharField(max_length=50, blank=True, null=True)
    Cpassw = models.CharField(max_length=50, blank=True, null=True)


class cartdb(models.Model):
    User = models.CharField(max_length=50, blank=True, null=True)
    Product = models.CharField(max_length=50, blank=True, null=True)
    Quantity = models.IntegerField(blank=True, null=True)
    Prices = models.IntegerField(blank=True, null=True)


class shipingdb(models.Model):
    User = models.CharField(max_length=50, blank=True, null=True)
    Email = models.CharField(max_length=50, blank=True, null=True)
    Address = models.CharField(max_length=100, null=True,blank=True)
    Phone = models.IntegerField(blank=True, null=True)
    Price = models.IntegerField(blank=True, null=True)
    Message = models.CharField(max_length=50, blank=True, null=True)