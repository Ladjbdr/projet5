#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
launch the pure_beurre program that aim to return a better
substitute of a selected product and allow to consult recorded
substitutes.
"""

import records

from database import Database
import sql_statements as sql

class Program:
    """
    this is the class responsible of launching the program.
    """
    welcome_msg = 'Welcome to Pure_Beurre!'
    
    def welcome(self):
        """
        startup message.
        """
        bold = "\033[1m"
        rst = "\033[0m"
        print(f"{bold}{self.welcome_msg}{rst}\n{'-' * len(self.welcome_msg)}")
        print(
            (
             f"{bold}What do you want to do?{rst}\n\n"
             "  1. Find a substitute.\n"
             "  2. Review substitutes.\n"
            )
        )

        
    def select_category(self, db):
        """
        this method allow the user to choose the category to find a substitute.
        """
        categories = db.query(sql.CATEGORIES_QUERY)
        print("\033[1mSelect a category: \033[0m")
        print()
        for category in categories:
            print(category.id, category.name)
        category = int(input())
        while category not in range(1, len(categories) + 1):
            category = int(input('\033[1mPlease, choose an existing category: \033[0m'))

        return category

    def select_product(self, db, category):
        """
        print the products of the selected category
        and allow the user to select one of them.
        """
        products = db.query(sql.PRODUCTS_QUERY % (category))
        print("\033[1mSelect a product: \033[0m")
        print()
        for id_, product in enumerate(products.as_dict(), 1):
             print(id_, product['name'])
        choice = int(input())
        while choice not in range(1, len(products) + 1):
            choice =  int(input('\033[1mPlease, choose an existing product: \033[0m'))
        product = products[choice - 1].name

        return product

    def select_substitute(self, db, category, product):
        """
        print the substitues and allow to
        choose one of them.
        """
        substitutes = db.query(
            sql.SUBTITUTES_QUERY % (category, product, category, product, category)
        )
        print('\033[1mSelect a Substitute: \033[0m')
        print()
        for id_, substitute in enumerate(substitutes.as_dict(), 1):
            print(id_, substitute['name'], "|", substitute['nutriscore'].upper())
        choice = int(input())
        while choice not in range(1, len(substitutes) + 1):
            choice =  int(input('\033[1mPlease, choose an existing substitue: \033[0m'))
        substitute = substitutes[choice - 1].name

        return substitute

    def rec_substitute(self, db, category, product, substitute):
        """
        this method print the details of the choosen substitue
        and prompt the user to record it or not.
        """
        query = db.query(sql.SUBSTITIUTE_DETAILS % (substitute))
        substitute_details = query.as_dict()[0]
        print('\033[1mSubstitue details: \033[0m')
        print()
        for key, value in substitute_details.items():
            print(key, ': ', value)
        print()
        response = input('\033[1mRecord to database? (Y/N)\n\033[0m')
        if response == 'y':
            db.query(
                sql.RECORD_SUBSTITUTE % (substitute, category)
            )

    def view_substitutes(self, db):
        """
        show all substitutes recorded by user.
        """
        substitutes = db.query(sql.SUBSTITUTES)
        print('\033[1mHere are your substitutes:\033[0m')
        print()
        #for row in substitutes:
        #    print(row.name, str(row.nutriscore).upper(), row.stores)
        print(substitutes.dataset)

def main():
    db = Database()
    session = db.connexion()
    program=Program()
    program.welcome()
    choice = int(input())

    if choice == 1:
        category = program.select_category(session)
        product = program.select_product(session, category)
        substitute = program.select_substitute(session, category, product)
        program.rec_substitute(session, category, product, substitute)

    if choice == 2:
        program.view_substitutes(session)

if __name__ == "__main__":
    main()
