from django.contrib.auth.models import User, Group
from rest_framework import serializers
from userImages.models import Image

class UserSerializer(serializers.ModelSerializer):
    images = serializers.PrimaryKeyRelatedField(many=True, queryset=Image.objects.all())
    class Meta:
        model = User
        fields = ['url','id', 'username', 'images']

class ImageSerializer(serializers.ModelSerializer):
    owner=serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Image
        fields = ['url', 'image', 'title', 'owner', 'price', 'discount', 'available']