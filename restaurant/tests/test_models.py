from django.test import TestCase
from restaurant.models import Menu
class MentuTest(TestCase):
     def test_get_item(self):
         item = Menu.objects.create(title="IceCream", price=80, inventory=100)
         self.assertEqual(item.title, "IceCream")
         self.assertEqual(item.price, 80)
         self.assertEqual(item.inventory, 100)