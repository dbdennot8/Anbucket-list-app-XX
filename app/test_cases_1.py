'''Unittesting the Bucket List App'''

# 1. Testing the User class

import unittest
from app_functionality import User


class TestUserModule(unittest.TestCase):
    '''Defines a class which once initialized allows testing to be
    done on app's Create Module'''

    def setUp(self):
        '''Initializes an instance of the class User for testing'''
        self.user = User("dennis@me.com", "dennot8", "why-me-tell-you?")

    def test_set_up(self):
        '''Test that initialized object is an instance of the class User'''
        self.assertIsInstance(self.user, User)

    def test_attribute_email(self):
        '''Test whether initialized object has the attribute email'''
        expected = "dennis@me.com"
        actual = self.user.email
        self.assertEqual(expected, actual)

    def test_attribute_user_name(self):
        '''Test whether initialized object has the attribute user_name'''
        expected = "dennot8"
        actual = self.user.user_name
        self.assertEqual(expected, actual)

    def test_attribute_password(self):
        '''Test whether initialized object has the attribute password'''
        expected = "why-me-tell-you?"
        actual = self.user.password
        self.assertEqual(expected, actual)

    def test_new_user_added_to_record(self):
        '''Test whether new user is appended to dict of authorized users'''
        new_user = self.user.register_user()
        self.assertIn(new_user.user_name, list(
            self.user.registered_users.keys()))

    def test_user_name_not_duplicated(self):
        '''Tests that a new user does not register using an existing user name'''
        new_user = self.user.register_user()
        new_user_2 = User("dennis@me.com", "dennot8", "why-me-tell-you?")
        new_user_2.register_user()
        self.assertNotIn(new_user_2, self.user.registered_users)

    def test_email_not_duplicated(self):
        '''Tests that a new user does not register using an existing email address'''
        new_user = self.user.register_user()
        new_user_2 = User("dennis@me.com", "dennot8", "why-me-tell-you?")
        new_user_2 = self.user.register_user()
        self.assertNotIn(new_user_2, self.user.registered_users)


if __name__ == 'main':
    unittest.main()
