#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
sql statements to create and fill database tables
"""

CREATE_CATEGORIES = """CREATE TABLE IF NOT EXISTS categories (
                       id integer AUTO INCREMENT PRIMARY KEY,
                       name text NOT NULL
                       );"""


CREATE_PRODUCTS = """CREATE TABLE IF NOT EXISTS products (
                     code,
                     name text NOT NULL,
                     ingredients text,
                     stores text NOT NULL,
                     nutrition_grade text,
                     category_id integer,
                     FOREIGN KEY (category_id) REFERENCES categories (id)
                     );"""


#CREATE_PRODUCT_CATEGORY = """CREATE TABLE IF NOT EXISTS product_category (
                             #product_id integer,
                             #category_id integer,
                             #PRIMARY KEY (product_id, category_id),
                             #FOREIGN KEY (product_id) REFERENCES products (id),
                             #FOREIGN KEY (category_id) REFERENCES categories (id)
                             #);"""


CREATE_NUTRITION_GRADE = """CREATE TABLE IF NOT EXISTS nutrition_grade (
                            id integer PRIMARY KEY,
                            grade text NOT NULL  
                            );"""


INSERT_INTO_CATEGORIES = """INSERT INTO categories (id, name)
                            VALUES (?, ?);"""


INSERT_INTO_PRODUCTS = """INSERT INTO products (code, name, ingredients, stores, nutrition_grade, category_id)
                          VALUES (?, ?, ?, ?, ?, ?);"""

INSERT_INTO_NUTRITION_GRADE = """INSERT INTO nutrition_grade (id, grade)
                                 VALUES (?, ?);"""
                                 