# -*- coding: utf-8 -*-
"""
Created on Fri Aug 13 18:53:04 2021

@author: alain
"""

from sanstitre1 import Api
from sanstitre2 import CATEGORIES
"remplir la base de donnée"
class Main():

    
    def __init__(self):
        for i in range(len(CATEGORIES)):
            category = CATEGORIES[i]
            self.api.get_products(category)
            i=i+1


Main()