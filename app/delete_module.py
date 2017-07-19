'''Module for Deleting an item from a bucket list'''

from update_module import Update


class Delete(Update):
    '''Boilerplate for initializing a delete instruction. Sub-classed from
    Update module.'''

    def __init__(self):
        '''Initializing Delete module with Inherit syntax'''
        super().__init__()

        # Set up a recycle bin
        self.recycle_bin = []

    def delete_item(self, title):
        '''Removes item with given title from bucket list'''
        del self.items[title]
        self.recycle_bin.append(title)
