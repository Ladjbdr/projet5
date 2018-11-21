#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""

"""
from sql_statements import *
from process_data import get_categories, get_category_products

import sqlite3

def create_connection(db_file='pure_beurre.db'):
    conn = sqlite3.connect(db_file)
    return conn


def create_table(conn, sql_statement):
    c = conn.cursor()
    c.execute(sql_statement)


def create_row(conn, sql_statement, entries):
    c = conn.cursor()
    c.executemany(sql_statement, entries)
    conn.commit()


def main():
    conn = create_connection()
    categories_ = get_categories()
    category = [(id, category['name']) for id, category in enumerate(categories_, 1)]
    grades = ('a', 'b', 'c', 'd', 'e')
    nutrition_grade = [(id, grade) for id, grade in enumerate(grades, 1)]
    product = []
    for idx in range(len(categories_)):
        products = get_category_products(categories_, idx + 1)
        element = [(product['code'],
				  product['product_name_fr'],
				  product['ingredients_text_fr'],
				  product['stores'],
                  product['nutrition_grade_fr']) 
				  for product in products 
                  if 'nutrition_grade_fr' in product.keys() 
                  and product['code'] 
                  and product['product_name_fr'] 
                  and product['ingredients_text_fr'] 
                  and product['stores'] 
                  and product['nutrition_grade_fr'] != '']
        product += element

    with conn:
        create_table(conn, CREATE_CATEGORIES)
        create_table(conn, CREATE_PRODUCTS)
        create_table(conn, CREATE_NUTRITION_GRADE)
        create_table(conn, CREATE_PRODUCT_CATEGORY)
        create_row(conn, INSERT_INTO_CATEGORIES, category)
        create_row(conn, INSERT_INTO_NUTRITION_GRADE, nutrition_grade)
        create_row(conn, INSERT_INTO_PRODUCTS, product)


if __name__=='__main__':
    main()
