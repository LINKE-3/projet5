# -*- coding: utf-8 -*-
"""
Created on Fri Aug 13 18:53:04 2021

@author: alain
"""

from Api import Api
from CATEGORIES import CATEGORIES
from Database import Database


class Main():
    "fill database"
    def __init__(self):
        self.api = Api()
        self.db = Database()
        for i in range(len(CATEGORIES)):
            category = CATEGORIES[i]
            self.api.get_products(category)
            self.db.insert_categories(category)


Main()
