from django.contrib import admin
from .models import Image
# Register your models here.

class AdminImageList(admin.ModelAdmin):
    list_display = ('image_tag', 'title', 'owner', 'price', 'discount', 'available')


admin.site.register(Image, AdminImageList)