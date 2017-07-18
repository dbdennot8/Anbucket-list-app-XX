'''
Module for creating a new user. Takes an email address, a user-name and
a password input by the user
'''


class Create(object):
    '''Boilerplate for creating a new user'''

    def __init__(self, email, user_name, password, bucket_list={}):
        '''Initialize a new user with given attributes'''
        self.email = email
        self.user_name = user_name
        self.password = password
        self.bucket_list = bucket_list

        # Keep record of authorized users, each user being an object.
        self.authorized_users = {}
