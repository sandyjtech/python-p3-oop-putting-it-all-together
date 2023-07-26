#!/usr/bin/env python3
#import ipdb

class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self._size = size
    def get_brand(self):
        return self._brand
    def get_size(self):
        return self._size
    def set_size(self, size):
        if type(size) in (int, float):
            print(f"Setting size to {size}")
        else:
            print("size must be an integer")
    def cobble(self):
        #create a new instance of the object
            self.condition = "New"          
            print("Your shoe is as good as new!")        
    size = property(get_size, set_size)     
        


  
#ipdb.set_trace()