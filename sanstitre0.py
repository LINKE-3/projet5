# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 15:00:32 2021

@author: alain
"""
import mysql.connector
from sanstitre2 import CATEGORIES 
import requests

"""
connexion = mysql.connector.connect(host = "localhost",user = "root",password = "",database="openff")
mycursor = connexion.cursor()
"""

class Database:
    def __init__(self):
        self.connector = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd="Mhbmhb9798"
        )
        
        self.mycursor = self.connector.cursor()
        self.create_database()
        self.create_table_produit()
        self.create_table_categories()
        
            
    def create_database(self):

        self.mycursor.execute("CREATE DATABASE IF NOT EXISTS openff")

        self.connector = mysql.connector.connect(
            host = "localhost",
            user = "root",
            passwd="Mhbmhb9798",
            database="openff"
        )
        
        self.mycursor = self.connector.cursor()
        
    def create_table_produit(self):

        table = "CREATE TABLE IF NOT EXISTS produit" +\
                "(id INTEGER(11) PRIMARY KEY NOT NULL AUTO_INCREMENT," +\
                "nom VARCHAR(100) NOT NULL," +\
                "nutriscore INT(3) NOT NULL," +\
                "category INT(3) NOT NULL)"
        self.mycursor.execute(table)
        
    def create_table_categories(self):
        table = "CREATE TABLE IF NOT EXISTS Categories" +\
                "(id INTEGER(2) PRIMARY KEY NOT NULL," +\
                "name VARCHAR(155) NOT NULL)"
        self.mycursor.execute(table)
        
    def insert_categories(self):
        cat_query = self.get_categories()
        if not cat_query:
            query = "INSERT INTO Categories (id, name) VALUES (%s, %s)"
            self.mycursor.executemany(query, CATEGORIES)
            self.connector.commit()

    def get_categories(self):
        query = "SELECT * FROM Categories"
        self.mycursor.execute(query)
        result = self.mycursor.fetchall()
        return result
    
    def insert_produit(self, data):

        query = "INSERT INTO Produit VALUES (NULL, %s, %s, %s)"
        self.mycursor.execute(query, data)
        self.connector.commit()


  
    def better_produit(self, data):
        
        url_prod = "https://fr.openfoodfacts.org/api/v0/produit/" + str(product_code) + ".json"
        request = requests.get(url_prod)
        product = request.json()["product"]
        url = "https://fr.openfoodfacts.org/cgi/search.pl?search_terms=" +\
              "" + product["categories"] + "&sort_by=unique_scans_n&page_size=100&json=1"
        request = requests.get(url)
        json = request.json()
        for i in range(len(json['products'])):
            try:
                alt_score = int(json['products'][i]['nutriments']['nutrition-score-fr'])
                prod_score = int(product['nutriments']['nutrition-score-fr'])
                if alt_score < prod_score:
                    return json['products'][i]
            except KeyError:
                pass
        return False


    def get_produits(self):
        query = "SELECT * FROM Produit"
        self.mycursor.execute(query)
        result = self.mycursor.fetchall()
        return result
    
    def create_table_alternative(self):

        query = "CREATE TABLE IF NOT EXISTS Alternatives" +\
                "(id INTEGER(2) PRIMARY KEY NOT NULL AUTO_INCREMENT," +\
                "name VARCHAR (155) NOT NULL," +\
                "nutriscore INTEGER(2) NOT NULL," +\
                "product_id INTEGER (2) NOT NULL UNIQUE," +\
                ")"
        self.mycursor.execute(query)

    def insert_alternative(self, data):
        query = "INSERT INTO Alternatives VALUES (NULL, %s, %s, %s, %s, %s)"
        try:
            self.mycursor.execute(query, data)
            self.connector.commit()
            print("Le produit :", data[0], "a bien été enregistré")
        except mysql.connector.errors.IntegrityError:
            print("Ce produit a déjà été enregistré")
        
        
    def get_saved_alternative(self, product):

        query = "SELECT * FROM Alternatives WHERE product_id = %s"
        data = (product[0], )
        self.mycursor.execute(query, data)
        return self.mycursor.fetchone()

        