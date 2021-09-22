# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 15:00:32 2021

@author: alain
"""
import mysql.connector
from CATEGORIES import CATEGORIES


class Database:
    """This class is used for every iteraction with the database,
    even creating it if it doesn't exist yet"""
    def __init__(self):
        """create the connector and create the database and
        all required elements if they don't exist yet
        """
        self.connector = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="Mhbmhb9798"
            )
        self.mycursor = self.connector.cursor()
        self.create_database()
        self.create_table_produit()
        self.create_table_categories()
        self.create_table_alternative()

    def create_database(self):
        """Create the database if it doesn't exist then update the connector"""
        self.mycursor.execute("CREATE DATABASE IF NOT EXISTS openff")
        self.connector = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="Mhbmhb9798",
            database="openff"
        )
        self.mycursor = self.connector.cursor(buffered=True)

    def create_table_produit(self):
        """Create the table produit"""
        table = "CREATE TABLE IF NOT EXISTS produit" +\
                "(id INTEGER(11) PRIMARY KEY NOT NULL AUTO_INCREMENT," +\
                "nom VARCHAR(255) NOT NULL," +\
                "code_bare VARCHAR(155) NOT NULL," +\
                "url VARCHAR(355) NOT NULL," +\
                "nutriscore INT(3) NOT NULL," +\
                "category INT(3) NOT NULL)"
        self.mycursor.execute(table)

    def create_table_categories(self):
        """Create the table categories"""
        table = "CREATE TABLE IF NOT EXISTS Categories" +\
                "(id INTEGER(2) PRIMARY KEY NOT NULL," +\
                "name VARCHAR(155) NOT NULL)"
        self.mycursor.execute(table)

    def insert_categories(self, category):
        """Insert the categories into their table"""
        cat_query = self.get_categories()
        if not cat_query:
            query = "INSERT INTO Categories (id, name) VALUES (%s, %s)"
            self.mycursor.executemany(query, CATEGORIES)
            self.connector.commit()

    def get_categories(self):
        """Return all the categories"""
        query = "SELECT * FROM Categories"
        self.mycursor.execute(query)
        result = self.mycursor.fetchall()
        return result

    def insert_produit(self, data):
        """Insert the produit into their table"""
        print(data)
        query = "INSERT INTO Produit VALUES (NULL, %s, %s, %s, %s, %s)"
        self.mycursor.execute(query, data)
        self.connector.commit()

    def better_produit(self, data):
        """find product with same category and better nutriscore table"""
        print(data)
        query = "SELECT * FROM Produit WHERE nutriscore < %s AND category = %s"
        self.mycursor.execute(query, (data[4], data[5]))
        return self.mycursor.fetchone()

    def get_produits(self, category):
        """Return all the produit from specific category"""
        query = "SELECT * FROM Produit WHERE category = %s"
        data = (category, )
        self.mycursor.execute(query, data)
        result = self.mycursor.fetchall()
        return result

    def get_product(self, prod_id):
        """get the id of an product"""
        query = "SELECT * FROM Products WHERE id = %s AND category = %s"
        data = (prod_id, )
        self.mycursor.execute(query, data)
        return self.mycursor.fetchone()

    def create_table_alternative(self):
        """Create the table alternative"""
        query = "CREATE TABLE IF NOT EXISTS Alternatives" +\
                "(id INTEGER(3) PRIMARY KEY NOT NULL AUTO_INCREMENT," +\
                "name VARCHAR (255) NOT NULL," +\
                "code_bare VARCHAR(155) NOT NULL," +\
                "url VARCHAR(255) NOT NULL," +\
                "nutriscore INTEGER(3) NOT NULL," +\
                "product_id INTEGER (3) NOT NULL UNIQUE" +\
                ")"
        self.mycursor.execute(query)

    def insert_alternative(self, data):
        """Insert the alternative into their table"""
        print(data)
        query = "INSERT INTO Alternatives VALUES (NULL, %s, %s, %s, %s, %s)"
        try:
            self.mycursor.execute(query, data)
            self.connector.commit()
            print("Le produit :", data[0], "a bien été enregistré")
        except mysql.connector.errors.IntegrityError:
            print("Ce produit a déjà été enregistré")

    def get_saved_alternative(self, product):
        """Return all the produit from specific category"""
        query = "SELECT * FROM Alternatives WHERE product_id = %s"
        data = (product[0], )
        self.mycursor.execute(query, data)
        return self.mycursor.fetchone()

    def get_saved_categories(self):
        """Return all the categorie from products register"""
        query = "SELECT DISTINCT Categories.id, Categories.name " +\
                "FROM Categories " +\
                "INNER JOIN produit ON Categories.id = produit.category " +\
                "INNER JOIN Alternatives On produit.id = Alternatives.product_id " +\
                "ORDER BY Categories.id ASC"
        self.mycursor.execute(query)
        return self.mycursor.fetchall()

    def get_saved_products(self, category):
        """return all products from a specific categorie"""
        query = "SELECT * FROM Produit " +\
                "INNER JOIN Alternatives ON Produit.id = Alternatives.product_id " +\
                "WHERE Produit.category = %s"
        data = (category, )
        self.mycursor.execute(query, data)
        return self.mycursor.fetchall()
