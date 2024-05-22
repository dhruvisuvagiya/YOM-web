from django.db import models
from django.forms import ModelForm
# Create your models here.

class reg(models.Model):
    Name=models.CharField(max_length=255)
    Email=models.EmailField(max_length=255)
    Password=models.CharField(max_length=255)

class form(models.Model):
    Title=models.CharField(max_length=255)
    Description=models.CharField(max_length=255)
    image=models.FileField(upload_to='media/')
    Default=models.BooleanField()

class sliderdata(ModelForm):
    class Meta:
        model = form
        fields = ["Title","Description","image","Default"]
    
class form_offer(models.Model):
    Image=models.ImageField(upload_to='media/',default=0)
    Icon_Title=models.CharField(max_length=255)
    Description=models.CharField(max_length=255)
    
class offerdata(ModelForm):
    class Meta:
        model = form_offer
        fields = ['Image','Icon_Title','Description']
 
class form_photos(models.Model):
    Image=models.FileField(upload_to='media/')
    Image_Title=models.CharField(max_length=255)
    Description=models.CharField(max_length=255)
    
class photosdata(ModelForm):
    class Meta:
        model = form_photos
        fields = ['Image','Image_Title', 'Description']
    
class form_post(models.Model):
    Image=models.FileField(upload_to='media/')
    Title=models.CharField(max_length=255)
    Description=models.CharField(max_length=255)
    
class postdata(ModelForm):
    class Meta:
        model = form_post
        fields = ['Image','Title','Description']

class form_contact(models.Model):
    Name=models.CharField(max_length=255)
    Email=models.EmailField()
    Subject=models.CharField(max_length=255)
    Message=models.CharField(max_length=500)
    
class form_category(models.Model):
    Category=models.CharField(max_length=255)
    
class add_work(models.Model):
    Category=models.CharField(max_length=255)
    File=models.FileField(upload_to='media/')
    
class workdata(ModelForm):
    class Meta:
        model = add_work
        fields = ['Category','File'] 

    