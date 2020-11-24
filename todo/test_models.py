from django.test import TestCase
from .models import Items


class TestModels(TestCase):

    def test_done_defaults_to_false(self):
        item = Items.objects.create(name='Test todo Item')
        self.assertFalse(item.done)

    def test_item_string_method_returns_name(self):
        item = Items.objects.create(name='Test todo Item')
        self.assertEqual(str(item), 'Test todo Item')
