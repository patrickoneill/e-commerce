from django.test import TestCase
from .models import Product

# Create your tests here.
class ProductTest(TestCase):
    ''' we define the test (must start with 'test')
    that we will run against our Post models'''
    
    def test_str(self):
        test_name = Product(name='A product')
        self.assertEqual(str(test_name), 'A product')
        
    