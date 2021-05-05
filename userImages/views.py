from django.shortcuts import render
from django.http import HttpResponse
from .models import Image

# Create your views here.
def images(request):

    images = Image.objects.all()
    output = ''
    for image in images:
        output = output + " "+ image.title + " " +image.owner + " " + str(image.price) + " " + str(image.discount) + " " + str(image.image)#+ " " + image.image+ " " +image.owner + " " + image.price + " " + image.discount + " "
    return HttpResponse(output)