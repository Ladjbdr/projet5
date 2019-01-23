#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
this module is responsible of creating the database.
"""

import os

import records

import sql_statements as sql
from data import DataSet


class Database:
    """

    """

    def __init__(self):
        """
        initialize session.
        """
        self.db_name = os.getenv('DB_NAME')
        self.user = os.getenv('DB_USER')
        self.passwd = os.getenv('DB_PASSWORD')

    def connexion(self):
        """
        connexion to database.
        """
        db = records.Database(
            f"""mysql+mysqlconnector://{self.user}:{self.passwd}@localhost:3306/
            {self.db_name}?charset=utf8mb4"""
        )

        db.query(f'USE {self.db_name}')
        
        return db


def main():
    #creating the structure of the database
    database = Database()
    session = database.connexion()
    session.query('DROP TABLE products')
    session.query('DROP TABLE categories')
    session.query(sql.CREATE_CATEGORIES)
    session.query(sql.CREATE_PRODUCTS)

    #creating the data to fill de DB
    data = DataSet()
    data.get_categories()
    categories = data.categories['tags'][5:10]
    products = []
    for key in range(len(categories)):
        elements = data.get_products(categories, key + 1)
        dataset = data.clean_dataset(elements)
        for product in dataset:
            products.append(product)
    
    #filling categories table
    for category in categories:
        name = category['name']
        session.query(sql.INSERT_INTO_CATEGORIES, name=name)
    

    #filling products table
    for product in products:
            name = product['name']
            nutriscore = product['nutriscore']
            stores = product['stores']
            subcategory = product['subcategory']
            category_id = product['category_id']
            session.query(
                sql.INSERT_INTO_PRODUCTS, 
                name=name, 
                nutriscore=nutriscore, 
                stores=stores, 
                subcategory=subcategory, 
                category_id=category_id
            )
    
if __name__ == '__main__':
    main()
