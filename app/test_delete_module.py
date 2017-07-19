'''Unittesting the Bucket List App'''

# 3. Testing the Delete Module

import unittest
from delete_module import Delete


class TestDeleteModule(unittest.TestCase):
    '''Defines a class which ones instantiated allows for testing of
    app's Delete Module'''

    def setUp(self):
        '''Initializes an instance of the class Delete for testing'''
        self.delete = Delete()

    def test_delete_method(self):
        '''Tests that delete method removes only one item from list of item'''
        bucket_list_item_1 = self.delete.add_bucket_list_item(
            'Marry', 'Before 2050')
        bucket_list_item_2 = self.delete.add_bucket_list_item(
            'Buy Car', 'Before I marry')
        items_in_list_before_delete = len(self.delete.items.keys())
        self.delete.delete_item('Marry')
        items_in_list_after_delete = len(self.delete.items.keys())
        change = items_in_list_before_delete - items_in_list_after_delete
        self.assertEqual(change, 1)

    def test_delete_method_2(self):
        '''Tests that delete method removes correct item from list'''
        bucket_list_item_1 = self.delete.add_bucket_list_item(
            'Marry', 'Before 2050')
        bucket_list_item_2 = self.delete.add_bucket_list_item(
            'Buy Car', 'Before I marry')
        self.delete.delete_item('Marry')
        items_not_deleted = list(self.delete.items.keys())
        self.assertNotIn('Marry', items_not_deleted)


if __name__ == 'main':
    unittest.main()
