'''App's functionality'''

from create_module import Create


def authorize_user(self, email, user_name, password):
    '''Append user with given attributes to a dict of authorised users'''
    new_user = Create(email, user_name, password)
    self.authorized_users[user_name] = new_user
