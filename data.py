#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Processing the data from OFF(open food facts) french products database.
"""
import json

import requests
import pandas as pd
import numpy as np


class DataSet:
    """
    this class is responsible of retrieviing data from its source, clean it in order to have a clean dataset.
    """
    url = 'https://fr.openfoodfacts.org/categories.json'
    search_url = 'https://fr.openfoodfacts.org/cgi/search.pl'
    index = [
            'product_name_fr', 
            'nutrition_grade_fr', 
            'stores', 
            ]

    def __init__(self):
        """
        init method of the dataset object.
        """
        self.categories = []
        self.products = []

    @classmethod
    def data_fetcher(cls, url, params=None):
        """
        this method is responsible of sending requests against the source.
        """
        response = requests.get(url, params)
        response_json = response.json()

        return response_json

    def get_categories(self):
        """
        this method is responsible of requesting all categories from source.
        """
        categories = self.data_fetcher(self.url)
        for category in categories['tags']:
            category['id'] = category['id'].replace('en:', '')
            del(category['url'], category['products'])

        self.categories = categories

        return self.categories

    def get_products(self, categories, key):
        """
        this method is responsible of fetching products of each category.
        """
        payload = {'json' :1,
               'action': 'process',
               'page_size': 40,
               'tagtype_0': 'categories',
               'tag_contains_0': 'contains',
               'tag_0': categories[key - 1]['id'],
              }
        category = self.data_fetcher(self.search_url, params=payload)
        for product in category['products']:
            product['category_id'] = key
        self.products = category['products']

        return self.products

    def clean_dataset(self, products):
        """

        """
        products = [
            {
                'product_name_fr': product.get('product_name_fr'),
                'nutrition_grade_fr': product.get('nutrition_grade_fr'),
                'stores': product.get('stores'),
                'category_id': product.get('category_id'),
            }
            for product in self.products
            if  bool(product.get('product_name_fr'))
            and bool(product.get('nutrition_grade_fr'))
            and bool(product.get('stores'))
            and bool(product.get('category_id')) != False
        ]

        return products


def main():
    """

    """
    data = DataSet()
    data.get_categories()
    categories = data.categories['tags'][5:10]
    products = []
    for key in range(len(categories)):
        elements = data.get_products(categories, key + 1)
        dataset = data.clean_dataset(elements)
        products += dataset
    
    for product in products:
        print(product)
        print()
    
    print(len(products))

if __name__=='__main__':
    main()
