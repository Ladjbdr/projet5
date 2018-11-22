#! /usr/bin/env python
# -*- coding: utf-8 -*-

from database import create_connection
from process_data import get_categories, get_category_products


import sqlite3

categories='\t1.Plats préparés \t2.Boissons sans alcool \t3.Aliments à base de fruits et légumes \t4.Céréales et pommes de terre \t5.Biscuits et gateaux'
print('welcome to pure beurre\n')
category_choice = int(input(f'\tchoose a category:\n\n\t{categories}\n'))
conn = create_connection()
#if category == '1':
with conn:
    c=conn.cursor()
    c.execute(f"""select name from products where category_id={category_choice}""")
    res_=c.fetchall()
    products_=[product[0] for product in res_]
    for product in enumerate(products_, 1):
        print('\t', product[0], product[1])
    product_choice=(int(input('\n choose a product: \n')))
    sql_req = f"""select * from products where name="{products_[product_choice - 1]}" """
    c.execute(sql_req)
    res_req=c.fetchone()
    _,name,ingredient,_,note,_ = res_req

    print('\nNom: ', name, '\nIngrédients: ', ingredient, '\nNote Nutritionelle: ', note.upper())
