'''Unittesting the Bucket List App'''

# 2. Testing the BucketList class
import unittest
from app_functionality import BucketList


class TestBucketListClass(unittest.TestCase):
    '''Defines a class which once initilaized allows tests to be
    done on app's Read Module'''

    def setUp(self):
        '''Initializes an instance of the class View for testing'''
        self.item = BucketList("Sail the Atlantic", "Before I Marry")

    def test_create_bucket_list_item_1(self):
        '''Test that create_an_item method appends to record of items'''
        self.item.create_an_item()
        self.assertIn("Sail the Atlantic", list(
            self.item.bucket_list_items.keys()))

    def test_create_bucket_list_items_2(self):
        '''Test that the create_an_item method does not duplicate items'''
        item_2 = BucketList("Sail the Atlantic", "Before I Marry")
        item_2.create_an_item()
        self.assertNotIn(item_2, list(
            self.item.bucket_list_items))

    def test_delete_method(self):
        '''Test that method removes item from bucket list items'''
        item_3 = BucketList("Marry the Queen", "Not Today")
        item_3.delete_item()
        self.assertNotIn(item_3,
                         self.item.bucket_list_items)


if __name__ == 'main':
    unittest.main()
