'''Unittesting the Bucket List App'''

# 2. Testing the BucketList class
import unittest
from app_functionality import BucketList, bucket_list_items


class TestBucketListClass(unittest.TestCase):
    '''Defines a class which once initilaized allows tests to be
    done on app's Read Module'''

    def setUp(self):
        '''Initializes an instance of the class View for testing'''
        self.item = BucketList("Sail the Atlantic", "Before I Marry")

    def test_add_items_to_list_1(self):
        '''Test that create_an_item method appends to record of items'''
        self.item.add_item_to_list()
        self.assertIn("Sail the Atlantic", list(
            bucket_list_items.keys()))

    def test_add_items_to_list_2(self):
        '''Test that the create_an_item method does not duplicate items'''
        item_2 = BucketList("Sail the Atlantic", "Before I Marry")
        items_before = len(bucket_list_items)
        item_2.add_item_to_list()
        items_after = len(bucket_list_items)
        self.assertEqual(items_before, items_after)

    def test_delete_method(self):
        '''Test that method removes item from bucket list items'''
        self.item.add_item_to_list()
        item_2 = BucketList("Marry the Queen", "Not Today")
        item_2.add_item_to_list()
        items_before_delete = len(list(bucket_list_items))
        self.item.delete_item()
        items_after_delete = len(list(bucket_list_items))
        difference = items_before_delete - items_after_delete
        self.assertNotIn(self.item, bucket_list_items)
        self.assertEqual(difference, 1)


if __name__ == 'main':
    unittest.main()
