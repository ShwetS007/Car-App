from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Cars(models.Model):
    model_name = models.CharField(max_length=30)
    mfg_year = models.DateField()
    car_img = models.ImageField(upload_to='img/',null=True,blank=True)
    color = models.CharField(max_length=15)
    no_of_seets = models.IntegerField(max_length=2)
    engine_type =models.CharField(max_length=15)
    price = models.IntegerField(max_length=20)