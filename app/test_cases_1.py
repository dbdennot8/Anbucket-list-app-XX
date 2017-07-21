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

    def test_register_user_method_1(self):
        '''Test whether new user is appended to dict of authorized users'''
        registered = self.user.register_user()
        self.assertIn(registered.user_name, list(
            self.user.registered_users.keys()))

    def test_register_user_method_2(self):
        '''Tests that a new user does not register using an existing user name'''
        self.user.register_user()
        users_before = len(list(self.user.registered_users))
        new_user_2 = User("val@me.com", "dennot8", "90210")
        new_user_2.register_user()
        users_after = len(list(self.user.registered_users))
        self.assertEqual(users_before, users_after)

    def test_register_user_method_3(self):
        '''Tests that a new user does not register using an existing email address'''
        self.user.register_user()
        users_before = len(list(self.user.registered_users))
        new_user_2 = User("dennis@me.com", "the-user", "me-pass-not")
        new_user_2.register_user()
        users_after = len(list(self.user.registered_users))
        self.assertEqual(users_before, users_after)

    def test_unregister_user_method(self):
        '''Tests that user is removed from dict of authorised users'''
        self.user.register_user()
        users_before = len(list(self.user.registered_users))
        self.user.unregister_a_user()
        users_after = len(list(self.user.registered_users))
        difference = users_before - users_after
        self.assertEqual(1, difference)


if __name__ == 'main':
    unittest.main()
