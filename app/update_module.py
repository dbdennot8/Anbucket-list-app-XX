'''
Module for creating a new bucket list item, once User is registered and logged in
'''


class Update(object):
    '''Boilerplate for defining a bucket list item'''

    def __init__(self):
        '''Initialize a bucket list item, having the following attributes'''

        # Initialize a list of bucket list items
        self.items = {}

    def add_bucket_list_item(self, title, badge):
        '''Appends bucket list items to a list of bucket list items'''
        if title in list(self.items.keys()):
            print('This item already exists in your bucket list.')
        else:
            new_item = (title, badge)
            self.items[title] = new_item
            return new_item
