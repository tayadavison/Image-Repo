from django.db import models

# Create your models here.

class Images(models.Model):
    image = models.ImageField(upload_to='pictures')
    title = models.CharField(max_length=100)
    owner = models.CharField(max_length=100)
    price = models.IntegerField()
    discount = models.IntegerField()