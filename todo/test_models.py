from django.test import TestCase
from .models import Item

# Create your tests here.


class TestModel(TestCase):

    def test_done_defaults_to_false(self):
       item = Item.objects.create(name='Test Todo Item')
       self.assertFalse(item.done)

    def test_item_string_method_returns_name(self):
        # create a Test Todo item
        item = Item.objects.create(name='Test Todo Item')
        # assert that this name is returned as a string
        self.assertEqual(str(item), 'Test Todo Item')