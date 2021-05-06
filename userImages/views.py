from django.shortcuts import render
from django.http import HttpResponse
from .models import Image
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions
from .api.permissions import IsOwnerOrReadOnly
from .api.serializers import UserSerializer, ImageSerializer


class ImageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows images to be viewed, created, edited and deleted.
    """
    queryset = Image.objects.all().order_by('price')
    serializer_class = ImageSerializer
    # Permissions to only allow owners edit and delete abilities
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows users to be viewed.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    # Permissions to only allow viewing users if the is_staff field is True
    permission_classes = [permissions.IsAdminUser]
