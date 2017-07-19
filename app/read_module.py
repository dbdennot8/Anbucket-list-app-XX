'''Module for Viewing the items existing on a user's Bucket List.
Based on the Update class'''

from update_module import Update


class Read(Update):
    '''Boilerplate for initializing Viewing bucket list'''

    def __init__(self):
        '''Initializing while inheriting from Update class'''
        super().__init__()

    def view_items(self):
        '''Display contents of Bucket List'''
        for item in self.items:
            return list(self.items.values())
