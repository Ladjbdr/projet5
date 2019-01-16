#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""

"""

import sqlite3

import records

db = records.Database('sqlite:///pure_beurre.db')

cat_ = db.query('select * from categories')
print('select a category:\n')
for row in cat_:
    print(row.id, row.name, end='\t', flush=True)
print(end='\n')
cat_choice = int(input('\nCategory: \n'))


prod_ = db.query(f'select name from products where category_id = {cat_choice}')
for id, prod in enumerate(prod_.as_dict(), 1):
    print(id, prod['name'])
prod_choice = int(input('select a product:'))




subst_ = db.query(f"""select name, nutrition_grade
                     from products
                     where category_id = {cat_choice}
                     and nutrition_grade <= (
                                             select nutrition_grade
                                             from products
                                             where name = "{prod_[prod_choice - 1].name}")
                     and product_group = (select product_group
                                          from products
                                          where name = "{prod_[prod_choice - 1].name}")
                     limit 3
                 """)
for id, subst in enumerate(subst_.as_dict(), 1):
    print(id, subst['name'], subst['nutrition_grade'])
subst_choice = int(input('select a substitue:'))

substitute = db.query(f'select * from products where name = "{subst_[subst_choice - 1].name}"')
sub_details = substitute.as_dict()[0]
for key, value in sub_details.items():
    print(key, ': ', value)

response = input('record to database? (Y/N)')
if response == 'y':
    db.query(f"""update products 
                 set substitute_id = (select rowid
                                      from products
                                      where name = "{substitute.first().name}")
                 where name = "{prod_[prod_choice - 1].name}" """)
    