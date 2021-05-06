from django.test import TestCase
from django.contrib.auth.models import User
from userImages.models import Image
from userImages.views import ImageViewSet, UserViewSet
from rest_framework.test import APIRequestFactory

# Tests the image views and the user views
class TestImageViewSet(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.factory = APIRequestFactory()
        cls.imageOwner = User.objects.create(username='owner', password="test1234")
        cls.notImageOwner = User.objects.create(username='notOwner', password="test1234")
        cls.image = Image.objects.create(title="testingKitten", image="pictures/CuteKittens.webp",price=57.49, discount=22.50, available=True, owner=cls.imageOwner )
        cls.image2 = Image.objects.create(title="testingKitten2", image="pictures/CuteKittens.webp",price=57.49, discount=22.50, available=True, owner=cls.imageOwner )
        pass

    def testGetImages(self):
        request = self.factory.get('/images/')
        response = ImageViewSet.as_view({'get':'list'})(request)
        self.assertEqual(response.status_code, 200)
    
    def testGetImageDetails(self):
        request = self.factory.get('/images/{self.image2.id}')
        response = ImageViewSet.as_view({'get':'retrieve'})(request, pk=self.image2.id)
        self.assertEqual(response.status_code, 200)

    def testCreateImage(self):
        request = self.factory.post('/images/', {'title': 'TestKitten2', 'image': 'pictures/CuteKittens.webp','price': '57.49', 'discount': '22.50', 'available': 'True'}, format='json')
        request.user = self.imageOwner

        response = ImageViewSet.as_view({'post':'list'})(request)
        self.assertEqual(response.status_code, 200)

    def testDeleteOwnedImage(self):
        request = self.factory.delete('/images/{self.image.id}')
        request.user = self.imageOwner

        response = ImageViewSet.as_view({'delete':'retrieve'})(request, pk=self.image.id)
        self.assertEqual(response.status_code, 200)
    
    def testDeleteNotOwnedImage(self):
        request = self.factory.delete('/images/{self.image2.id}')
        request.user = self.notImageOwner

        response = ImageViewSet.as_view({'delete':'retrieve'})(request, pk=self.image.id)
        self.assertEqual(response.status_code, 403)

    def testPutOwnedImage(self):
        request = self.factory.put('/images/{self.image2.id}', {'available': 'False'}, format='json')
        request.user = self.imageOwner

        response = ImageViewSet.as_view({'put':'retrieve'})(request, pk=self.image.id)
        self.assertEqual(response.status_code, 200)
    
    def testPutNotOwnedImage(self):
        request = self.factory.put('/images/{self.image2.id}', {'title': 'update'}, format='json')
        request.user = self.notImageOwner

        response = ImageViewSet.as_view({'put':'retrieve'})(request, pk=self.image.id)
        self.assertEqual(response.status_code, 403)

class TestUserViewSet(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.factory = APIRequestFactory()
        cls.notStaffUser = User.objects.create(username='notAdmin', password="test1234")
        cls.staffUser = User.objects.create(username='testAdmin', password="test1234", is_staff=True)
        pass

    def testAdminGetUsers(self):
        request = self.factory.get('/users/')
        request.user = self.staffUser
        response = UserViewSet.as_view({'get':'list'})(request)
        self.assertEqual(response.status_code, 200)
    
    def testAdminGetUserDetails(self):
        request = self.factory.get('/images/{self.notStaffUser.id}')
        request.user = self.staffUser
        response = UserViewSet.as_view({'get':'retrieve'})(request, pk=self.notStaffUser.id)
        self.assertEqual(response.status_code, 200)
    
    def testNotAdminGetUsers(self):
        request = self.factory.get('/users/')
        request.user = self.notStaffUser
        response = UserViewSet.as_view({'get':'list'})(request)
        self.assertEqual(response.status_code, 403)
    
    def testNotAdminGetUserDetails(self):
        request = self.factory.get('/images/{self.notstaffUser.id}')
        request.user = self.notStaffUser
        response = UserViewSet.as_view({'get':'retrieve'})(request,self.notStaffUser.id)
        self.assertEqual(response.status_code, 403)