from django.urls import path
from . import views

urlpatterns = [
    path('', views.images, name='images'),
]

