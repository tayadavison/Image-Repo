from django.test import TestCase
from userImages.models import Image
from django.contrib.auth.models import User
from django.utils.html import mark_safe

# Tests the custom display methods from the Image model
class TestViews(TestCase):
    @classmethod
    def setUpTestData(cls):
        testUser = User.objects.create(username='test1234', password="test1234")
        Image.objects.create(title="testingKitten", image="pictures/CuteKittens.webp",price=57.49, discount=22.50, available=True, owner=testUser )
        Image.objects.create(title="testingKitten2", image="pictures/CuteKittens.webp",price=57.49, discount=0, available=True, owner=testUser )
        pass

    def testPriceDisplay(self):
        kittenImage = Image.objects.get(title="testingKitten")
        priceValue = kittenImage.priceDisplay()
        self.assertEqual(priceValue, '$57.49')

    def testDiscountPriceDisplay(self):
        kittenImage = Image.objects.get(title="testingKitten")
        discountPriceValue = kittenImage.discountPriceDisplay()
        self.assertEqual(discountPriceValue, '$34.99')
    
    def testDiscountPriceDisplayNoDiscount(self):
        kittenImage = Image.objects.get(title="testingKitten2")
        discountPriceValue = kittenImage.discountPriceDisplay()
        self.assertEqual(discountPriceValue, '---')
    
    def testImageDisplay(self):
        kittenImage = Image.objects.get(title="testingKitten")
        imageTag = kittenImage.imageDisplay()
        self.assertEqual(imageTag, '<img src="/pictures/CuteKittens.webp" width="150"/>')
