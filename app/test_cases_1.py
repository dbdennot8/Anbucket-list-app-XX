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
        new_user_2 = self.user.register_user()
        self.assertNotIn(new_user_2, self.user.registered_users)

    def test_register_user_method_3(self):
        '''Tests that a new user does not register using an existing email address'''
        self.user.register_user()
        new_user_2 = self.user.register_user()
        self.assertNotIn(new_user_2, self.user.registered_users)


if __name__ == 'main':
    unittest.main()
