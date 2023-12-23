from django.db import models

# Create your models here.
class contactmedb(models.Model):
    name = models.CharField(max_length=20,blank=True,null=True)
    email =models.CharField(max_length=20,blank=True,null=True)
    message = models.CharField(max_length=200,blank=True,null=True)

class Resume(models.Model):
    file = models.FileField(null=True,upload_to="files")