from django.db import models
from django.utils.html import mark_safe

# Create your models here.

class Image(models.Model):
    image = models.ImageField(upload_to='pictures')
    title = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=6)
    discount = models.DecimalField(decimal_places=2, max_digits=6)
    available = models.BooleanField(default=True)
    owner = models.ForeignKey('auth.User', related_name='images', on_delete=models.CASCADE)


    def image_tag(self):
        return mark_safe('<img src="{0}" width = "150"/>'.format(self.image.url))
    image_tag.short_description = 'Image'