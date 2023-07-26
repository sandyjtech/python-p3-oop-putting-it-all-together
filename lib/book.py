#!/usr/bin/env python3
#import ipdb

class Book:        
    def __init__(self, title, page_count):
        self.title = title
        self._page_count = page_count

    def get_page_count(self):
        return self._page_count
           
    def set_page_count(self, page_count):
        if type(page_count) in (int, float):
            print(f"Setting page_count to {page_count}.")
            #use underscore to reference what is in the init
            self._page_count = page_count
        else:
            print("page_count must be an integer")        
        
    def turn_page(self):
            print("Flipping the page...wow, you read fast!")
            
    page_count = property(get_page_count, set_page_count, turn_page)
    #ipdb.set_trace()       
    