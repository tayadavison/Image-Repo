from django.test import TestCase
from userImages.models import Image
from django.contrib.auth.models import User
from django.utils.html import mark_safe

# Create your tests here.

class TestViews(TestCase):
    @classmethod
    def setUpTestData(cls):
        testUser = User.objects.create(username='test1234', password="test1234")
        Image.objects.create(title="testingKitten", image="pictures/CuteKittens.webp",price=57.49, discount=22.50, available=True, owner=testUser )
        pass

    def testPriceDisplay(self):
        kittenImage = Image.objects.get(title="testingKitten")
        priceValue = kittenImage.format_price()
        self.assertEqual(priceValue, '$57.49')

    def testDiscountPriceDisplay(self):
        kittenImage = Image.objects.get(title="testingKitten")
        discountPriceValue = kittenImage.discount_price()
        self.assertEqual(discountPriceValue, '$34.99')
    
    def testImageFormat(self):
        kittenImage = Image.objects.get(title="testingKitten")
        imageTag = kittenImage.image_tag()
        self.assertEqual(imageTag, '<img src="/pictures/CuteKittens.webp" width="150"/>')
