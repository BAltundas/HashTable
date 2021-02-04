# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 00:46:59 2021
Ecxample of Has Table
@author: Bilgin
"""

class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]
        
    def get_hash(self,key):
        h=0
        for char in key:
            h = h + ord(char) # or returns ord number 
                            #for each char
        return h% self.MAX
    
    def __setitem__(self,key, value):
        h= self.get_hash(key)
        self.arr[h] = value
        
    def __getitem__(self,key):
        h=self.get_hash(key)
        return self.arr[h]

