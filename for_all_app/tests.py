from django.test import TestCase
from .models import Products

# Create your tests here.

class MenuTest(TestCase):
    
    def test_get_item(self):
        menu_item = Products.objects.create(title="Milk", 
                                            price=2.5,
                                            quantity = 106,
                                            description= "fresh milk",
                                            category = "drink")
        
        self.assertEqual(str(menu_item), 'Milk')

