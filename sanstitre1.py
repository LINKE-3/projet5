# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 15:18:20 2021

@author: alain
"""

import requests
from sanstitre0 import Database


class Api:
    def get_products(self, category):
    
        params = {"search_terms":category[1],"json":1,"page_size":200}  
        donnees = requests.get("https://fr.openfoodfacts.org/cgi/search.pl",params = params)
        db = Database()
        json = donnees.json()  
        ite = 0
        quant = 100
        
        while ite < quant:
            try:
                #checking if the product has a nutriscore
        
                data = (
                    json ["products"][ite]['product_name_fr'],
                    json ["products"][ite]['id'],
                    json ["products"][ite]["url"],
                    json["products"][ite]['nutriments']['nutrition-score-fr'],
                    category[0]
                )
                db.insert_produit(data)
        
            except KeyError:
                quant += 1
            ite += 1


    

