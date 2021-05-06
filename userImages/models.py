from django.db import models
from django.utils.html import mark_safe

class Image(models.Model):
    image = models.ImageField(upload_to='pictures')
    title = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=6)
    discount = models.DecimalField(decimal_places=2, max_digits=6)
    available = models.BooleanField(default=True)
    owner = models.ForeignKey('auth.User', related_name='images', on_delete=models.CASCADE)

    #Display image in the admin panel
    def imageDisplay(self):
        return mark_safe('<img src="{0}" width="150"/>'.format(self.image.url))
    imageDisplay.short_description = 'Image'

    #format price to have '$'
    def priceDisplay(self):
        return '${0:.2f}'.format(self.price)
    priceDisplay.short_description = "Price"

    #Calculate discount price or display '---' to indicate no discount
    def discountPriceDisplay(self):
        if self.discount == 0:
            return '---'
        return '${0:.2f}'.format(self.price-self.discount)
    discountPriceDisplay.short_description = "Discount Price"