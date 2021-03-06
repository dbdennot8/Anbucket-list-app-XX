'''Bucket List App Functionality'''

# Details of users already registered
registered_users = {}

# Initialize a record of items in bucket list
bucket_list_items = {}

class User(object):
    '''Boilerplate for creating a new user'''

    def __init__(self, email, user_name, password):
        '''Initialize a new user with given attributes'''
        self.email = email
        self.user_name = user_name
        self.password = password

        # emails already in use
        self.all_registered_emails = []

    def register_user(self):
        '''Appends a new user to a record of users with access to the app'''
        if self.user_name in list(registered_users.keys()):
            return 'This user-name is already in use. Please try another.'
        elif self.email in self.all_registered_emails:
            return 'This email is already in use.'
        else:
            new_user = User(self.email, self.user_name, self.password)
            registered_users[self.user_name] = new_user
            self.all_registered_emails.append(self.email)
            return new_user

    def unregister_a_user(self):
        '''Method removes user from list of authorised users'''
        if self.user_name in list(registered_users.keys()):
            del registered_users[self.user_name]
        else:
            pass


class BucketList(object):
    '''Boilerplate for creating a bucket list'''



    def __init__(self, title, badge):
        self.title = title
        self.badge = badge

    def add_item_to_list(self):
        '''Append an item to the list of bucket list items'''
        if self.title in list(bucket_list_items.keys()):
            return 'That item is already in your bucket list'
        else:
            new_item = BucketList(self.title, self.badge)
            bucket_list_items[self.title] = new_item
            return new_item

    def delete_item(self):
        '''Removes a given item from the bucket list'''
        if self.title in list(bucket_list_items.keys()):
            del bucket_list_items[self.title]
        else:
            pass
