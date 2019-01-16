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
                     category_id INT UNSIGNED,
                     substitute_id INT UNSIGNED,
                     PRIMARY KEY (id),
                     FOREIGN KEY (category_id) REFERENCES categories (id),
                     FOREIGN KEY (substitute_id) REFERENCES products (id)
                     )"""

INSERT_INTO_CATEGORIES = """INSERT INTO categories (name)
                            VALUES (:name)"""

INSERT_INTO_PRODUCTS = """INSERT INTO products (name, nutriscore, stores, category_id)
                          VALUES (:name, :nutriscore, :stores, :category_id)"""

                                 