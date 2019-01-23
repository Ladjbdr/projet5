#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
sql statements to create and fill database tables
"""

CREATE_CATEGORIES = """CREATE TABLE IF NOT EXISTS categories (
                       id INT UNSIGNED NOT NULL AUTO_INCREMENT,
                       name VARCHAR(255) NOT NULL,
                       PRIMARY KEY (id)
                       )"""

CREATE_PRODUCTS = """CREATE TABLE IF NOT EXISTS products (
                     id INT UNSIGNED NOT NULL AUTO_INCREMENT,
                     name VARCHAR(255) NOT NULL,
                     nutriscore CHAR(1),
                     stores VARCHAR(255),
                     subcategory VARCHAR(255),
                     category_id INT UNSIGNED,
                     issubstitute VARCHAR(5),
                     PRIMARY KEY (id),
                     FOREIGN KEY (category_id) REFERENCES categories (id)
                     )"""

INSERT_INTO_CATEGORIES = """INSERT INTO categories (name)
                            VALUES (:name)"""

INSERT_INTO_PRODUCTS = """INSERT INTO products (name, nutriscore, stores, subcategory, category_id)
                          VALUES (:name, :nutriscore, :stores, :subcategory, :category_id)"""

CATEGORIES_QUERY = "select * from categories"

PRODUCTS_QUERY = "select name from products where category_id = %d"

SUBTITUTES_QUERY = """select name, nutriscore
                     from products
                     where category_id = %d
                     and nutriscore <= (
                                        select nutriscore from products
                                        where name = "%s"
                                        and category_id = %d
                                        )
                     and subcategory = (
                                          select subcategory
                                          from products
                                          where name = "%s"
                                          and category_id = %d
                                         )
                     ORDER BY nutriscore ASC                    
                     limit 3
                 """

SUBSTITIUTE_DETAILS = """select name, nutriscore, stores 
                         from products
                         where name = "%s"
                         """

RECORD_SUBSTITUTE = """update products 
                       set issubstitute="True"
                       where name = "%s"
                       and category_id = %d
                       """

SUBSTITUTES = """select name, nutriscore, stores
                 from products
                 where issubstitute = "True"
                 """                                 