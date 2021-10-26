from django.db import models
from django.db.models import aggregates

# Create your models here.
class partner(models.Model):
    partner_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    father_name=models.CharField(max_length=100)
    mother_name=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    cast=models.CharField(max_length=100)
    religion=models.CharField(max_length=100)
    age=models.IntegerField()
    description=models.TextField(max_length=1000)
    tag=models.CharField(max_length=100)
    gender=models.CharField(max_length=50)
    qualifications=models.CharField(max_length=500)
    occupation=models.CharField(max_length=200)
    height=models.CharField(max_length=50)
    image1=models.ImageField(upload_to='images',default="")
    image2=models.ImageField(upload_to='images',default="")
    image3=models.ImageField(upload_to='images',default="")

    def __str__(self):
        return self.name
