'''Unittesting the Bucket List App'''

# 1. Testing the Create Module

import unittest
from create_module import User


class TestCreateModule(unittest.TestCase):
    '''Defines a class which once initialized allows testing to be
    done on app's Create Module'''

    def setUp(self):
        '''Initializes an instance of the class User for testing'''
        self.user = User()

    def test_set_up(self):
        '''Test that initialized object is an instance of the class User'''
        self.assertIsInstance(self.user, User)

    def test_attribute_email(self):
        '''Test whether initialized object has the attribute email'''
        new_user = self.user.register_new_user(
            "me@andela.com", "dennot8", "why-me-tell-you?")
        expected = "me@andela.com"
        actual = new_user[0]
        self.assertEqual(expected, actual)

    def test_attribute_user_name(self):
        '''Test whether initialized object has the attribute user_name'''
        new_user = self.user.register_new_user(
            "me@andela.com", "dennot8", "why-me-tell-you?")
        expected = "dennot8"
        actual = new_user[1]
        self.assertEqual(expected, actual)

    def test_attribute_password(self):
        '''Test whether initialized object has the attribute password'''
        new_user = self.user.register_new_user(
            "me@andela.com", "dennot8", "why-me-tell-you?")
        expected = "why-me-tell-you?"
        actual = new_user[2]
        self.assertEqual(expected, actual)

    def test_new_user_added_to_record(self):
        '''Test whether new user is appended to dict of authorized users'''
        new_user = self.user.register_new_user(
            "me@andela.com", "dennot8", "why-me-tell-you?")
        self.assertIn(new_user[1], self.user.registered_users.keys())

    def test_user_name_not_duplicated(self):
        '''Tests that a new user does not register using an existing user name'''
        new_user = self.user.register_new_user(
            "me@andela.com", "dennot8", "why-me-tell-you?")
        new_user_2 = self.user.register_new_user(
            "metoo@andela.com", "dennot8", "why-me-tell-you?")
        self.assertNotIn(new_user_2, self.user.registered_users)

    def test_email_not_duplicated(self):
        '''Tests that a new user does not register using an existing email address'''
        new_user = self.user.register_new_user(
            "me@andela.com", "dennot8", "why-me-tell-you?")
        new_user_2 = self.user.register_new_user(
            "me@andela.com", "khalegi", "why-me-tell-you?")
        self.assertNotIn(new_user_2, self.user.registered_users)


if __name__ == 'main':
    unittest.main()
