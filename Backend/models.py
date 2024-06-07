from django.db import models


# Create your models here.
class categorydb(models.Model):
    Cname = models.CharField(max_length=50, null=True, blank=True)
    Des = models.CharField(max_length=50, null=True, blank=True)
    Image = models.ImageField(upload_to="Product_Images", null=True, blank=True)


class productdb(models.Model):
    Category = models.CharField(max_length=50, null=True, blank=True)
    Pname = models.CharField(max_length=50, null=True, blank=True)
    Description = models.CharField(max_length=50, null=True, blank=True)
    Price = models.IntegerField(null=True, blank=True)
    Pimage = models.ImageField(upload_to="P_Images", null=True, blank=True)
