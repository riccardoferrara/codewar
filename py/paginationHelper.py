# For this exercise you will be strengthening your page-fu mastery. You will complete the PaginationHelper class, which is a utility class helpful for querying paging information related to an array.

# The class is designed to take in an array of values and an integer indicating how many items will be allowed per each page. The types of values contained within the collection/array are not relevant.

# The following are some examples of how this class is used:

# helper = PaginationHelper(['a','b','c','d','e','f'], 4)
# helper.page_count() # should == 2
# helper.item_count() # should == 6
# helper.page_item_count(0)  # should == 4
# helper.page_item_count(1) # last page - should == 2
# helper.page_item_count(2) # should == -1 since the page is invalid

# # page_index takes an item index and returns the page that it belongs on
# helper.page_index(5) # should == 1 (zero based index)
# helper.page_index(2) # should == 0
# helper.page_index(20) # should == -1
# helper.page_index(-10) # should == -1 because negative indexes are invalid

# TODO: complete this class

import codewars_test as test
import math

class PaginationHelper:

    # The constructor takes in an array of items and a integer indicating
    # how many items fit within a single page
    def __init__(self, collection, items_per_page):
        self.collection = collection
        self.items_per_page = items_per_page
        print('collection: %s' % collection)
        print('items per page: %d' % items_per_page)
        self.item_count()
        self.page_count()

    # returns the number of items within the entire collection
    def item_count(self):
        self.items_number = len(self.collection)
        return self.items_number

    # returns the number of pages
    def page_count(self):
        self.pages_number = math.ceil(len(self.collection) / self.items_per_page)
        return self.pages_number

    # returns the number of items on the current page. page_index is zero based
    # this method should return -1 for page_index values that are out of range
    def page_item_count(self, page_index):
        if page_index +1 > self.pages_number:
            return -1
        if page_index + 1< self.pages_number:
            return self.items_per_page
        if page_index +1 == self.pages_number:
            return len(self.collection) % self.items_per_page

    # determines what page an item is on. Zero based indexes.
    # this method should return -1 for item_index values that are out of range
    def page_index(self, item_index):
        if not hasattr(self, 'items_number'):
            self.item_count()
        if (item_index > self.items_number-1) or (item_index < 0):
            return -1
        else:
            return round(item_index / self.items_per_page, 0 )


collection = range(1,25)
helper = PaginationHelper(collection, 10)

test.assert_equals(helper.page_count(), 3, 'page_count is returning incorrect value.')
test.assert_equals(helper.page_index(23), 2, 'page_index returned incorrect value')
test.assert_equals(helper.item_count(), 24, 'item_count returned incorrect value')

helper = PaginationHelper(['a','b','c','d','e','f'], 4)
test.assert_equals(helper.page_count(), 2)
test.assert_equals(helper.item_count(), 6)
test.assert_equals(helper.page_item_count(0), 4)
test.assert_equals(helper.page_item_count(1), 2)
test.assert_equals(helper.page_item_count(2), -1)
test.assert_equals(helper.page_index(7), -1)
test.assert_equals(helper.page_index(0), 0)
test.assert_equals(helper.page_index(6), -1)