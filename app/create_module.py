'''
Module for creating a new user. Takes an email address, a user-name and
a password input by the user
'''


class User(object):
    '''Boilerplate for creating a new user'''

    def __init__(self):
        '''Initialize a new user with given attributes'''
        # Details of users already registered
        self.registered_users = {}

        # emails already in use
        self.all_registered_emails = []

    def register_new_user(self, email, user_name, password):
        '''Appends a new user to a record of users with access to the app'''
        if user_name in list(self.registered_users.keys()):
            print('This user-name is already in use. Please try another.')
        elif email in self.all_registered_emails:
            print('This email is already in use.')
        else:
            new_user = (email, user_name, password)
            self.registered_users[user_name] = new_user
            self.all_registered_emails.append(email)
            return new_user
