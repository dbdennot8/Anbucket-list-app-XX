'''Unittesting the Bucket List app'''

import unittest
from create_module import Create



class TestBucketListfeatures(unittest.TestCase):
    '''Defines a class which once initialized allows testing to be done on app's methods'''

    def setUp(self):
        '''Initializes an instance of the class Create for testing'''
        self.demo = Create("me@example.com", "dennot8", "12345")

    def test_intializes_instant_of_class_create(self):
        '''Test that initialized object is an instance of the class Create'''
        self.assertIsInstance(self.demo, Create)

    def test_attribute_user_name(self):
        '''Test whether initialized object has attribute user_name'''
        expected = "dennot8"
        actual = self.demo.user_name
        self.assertEqual(expected, actual)

    def test_attribute_bucket_list(self):
        '''Test whether initialized object has attribute bucket_list'''
        expected = {}
        actual = self.demo.bucket_list
        self.assertEqual(expected, actual)


if __name__ == 'main':
    unittest.main()
