'''
Module for creating a new user. Takes an email address, a user-name and
a password input by the user
'''

# Keep record of authorized users, each user being an object.
authorized_users = {}


class Create(object):
    '''Boilerplate for creating a new user'''

    def __init__(self, email, user_name, password, bucket_list=[]):
        '''Initialize a new user with given attributes'''
        self.email = email
        self.user_name = user_name
        self.password = password
        self.bucket_list = bucket_list

    def authorize_user(self, email, user_name, password):
        '''Append user with given attributes to a dict of authorised users'''
        new_user = Create(email, user_name, password)
        authorized_users[user_name] = new_user


demo = Create("you@example.com", "t_nane", "why-tell-you?")
print()
print(demo.email)
print(demo.user_name)
print(demo.password)
print()
print(authorized_users)
print()
