from django.test import TestCase
from django.contrib.auth.models import User
from userImages.models import Image
from userImages.api.permissions import IsOwnerOrReadOnly
from rest_framework.test import APIRequestFactory

class apiPermissionsTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.factory = APIRequestFactory()
        cls.imageOwner = User.objects.create(username='owner', password="test1234")
        cls.notImageOwner = User.objects.create(username='notOwner', password="test1234")
        Image.objects.create(title="testingKitten", image="pictures/CuteKittens.webp",price=57.49, discount=22.50, available=True, owner=cls.imageOwner )
        pass

    def testOwnerGetPermission(self):
        image = Image.objects.get(title="testingKitten")
        request = self.factory.get('/')
        request.user = self.imageOwner

        permission = IsOwnerOrReadOnly()
        self.assertTrue(permission.has_object_permission(request, None, image))

    def testOwnerPutPermission(self):
        image = Image.objects.get(title="testingKitten")
        request = self.factory.put('/')
        request.user = self.imageOwner

        permission = IsOwnerOrReadOnly()
        self.assertTrue(permission.has_object_permission(request, None, image))

    def testOwnerDeletePermission(self):
        image = Image.objects.get(title="testingKitten")
        request = self.factory.delete('/')
        request.user = self.imageOwner

        permission = IsOwnerOrReadOnly()
        self.assertTrue(permission.has_object_permission(request, None, image))

    def testNotOwnerGetPermission(self):
        image = Image.objects.get(title="testingKitten")
        request = self.factory.get('/')
        request.user = self.notImageOwner

        permission = IsOwnerOrReadOnly()
        self.assertTrue(permission.has_object_permission(request, None, image))

    def testNotOwnerPutPermission(self):
        image = Image.objects.get(title="testingKitten")
        request = self.factory.put('/')
        request.user = self.notImageOwner

        permission = IsOwnerOrReadOnly()
        self.assertFalse(permission.has_object_permission(request, None, image))

    def testNotOwnerDeletePermission(self):
        image = Image.objects.get(title="testingKitten")
        request = self.factory.delete('/')
        request.user = self.notImageOwner

        permission = IsOwnerOrReadOnly()
        self.assertFalse(permission.has_object_permission(request, None, image))

