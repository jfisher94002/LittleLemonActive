from django.test import TestCase

from ..models import MenuItem


class MenuItemTest(TestCase):
    def test_get_item(self):
        item = MenuItem.objects.create(title="IceCream", price=80, inventory=100)
        print(f"Created item: {item.title} : {item.price}")
        self.assertEqual(item.get_item(), "IceCream : 80")
