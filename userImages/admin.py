from django.contrib import admin
from .models import Image
# Register your models here.

class AdminImageList(admin.ModelAdmin):
    list_display = ('imageDisplay', 'title', 'owner', 'priceDisplay', 'discountPriceDisplay', 'available')


admin.site.register(Image, AdminImageList)