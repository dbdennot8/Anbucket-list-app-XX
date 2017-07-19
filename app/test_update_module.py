'''Unittesting the Bucket List App'''

# 2. Testing the Update Module

import unittest
from update_module import Update


class TestUpdateModule(unittest.TestCase):
    '''Defines a class which once initilaized allows tests to be 
    done on app's Read Module'''

    def setUp(self):
        '''Initializes an instance of the class View for testing'''
        self.item = Update()

    def test_attribute_title(self):
        '''Test whether the bucket list item has a title as an attribute'''
        new_item = self.item.add_bucket_list_item(
            "Sail the Atlantic", "Before I Marry")
        expected = 'Sail the Atlantic'
        actual = new_item[0]
        self.assertEqual(actual, expected)

    def test_attribute_badge(self):
        '''Test whether item has a badge as one of its attributes'''
        new_item = self.item.add_bucket_list_item(
            "Sail the Atlantic", "Before I Marry")
        expected = 'Before I Marry'
        actual = new_item[1]
        self.assertEqual(actual, expected)

    def test_add_bucket_list_method(self):
        '''Test whether the add_bucket_list_item method appends to record of items'''
        new_item = self.item.add_bucket_list_item(
            "Sail the Atlantic", "Before I Marry")
        self.assertIn(new_item[0], list(self.item.items.keys()))

    def test_item_not_duplicated(self):
        '''Test that method does not duplicate bucket list items'''
        initial_number_of_items = len(list(self.item.items.keys()))
        new_item = self.item.add_bucket_list_item(
            "Sail the Atlantic", "Before I Marry")
        new_item_2 = self.item.add_bucket_list_item(
            "Sail the Atlantic", "Before I Marry")
        final_number_of_items = len(list(self.item.items.keys()))
        added_items = final_number_of_items - initial_number_of_items
        self.assertNotEqual(added_items, 2)
