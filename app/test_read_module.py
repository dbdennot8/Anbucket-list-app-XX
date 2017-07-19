'''Unittesting the Bucket List App'''

# 4. Testing the View Module

import unittest
from read_module import Read


class TestViewModule(unittest.TestCase):
    '''Defines a class which once initilaized allows tests to be
    done on app's Read Module'''

    def setUp(self):
        '''Initiliaze an instance of View for testing'''
        self.view = Read()

    def test_view_displays_all_items(self):
        '''Test that all items in a bucket list are displayed'''
        item_1 = self.view.add_bucket_list_item('Marry', 'Before I turn 80')
        item_2 = self.view.add_bucket_list_item('Buy bike', 'After I marry')
        item_3 = self.view.add_bucket_list_item(
            'Scuba dive somewhere', 'During honeymoon')
        displayed = len(list(self.view.view_items()))
        actual = len(list(self.view.items.keys()))
        self.assertEqual(displayed, actual)


if __name__ == 'main':
    unittest.main()
