#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Processing the data from OFF(open food facts) french products database.
"""
import json
import requests

def get_categories():
    """
    retrieving a sample of 5 categories with ids, urls, names and product
    numbers for each category.
    """
    url = 'https://fr.openfoodfacts.org/categories.json'
    response = requests.get(url)
    res_json = response.json()
    categories = res_json['tags'][:5]

    return categories


def get_category_products(categories, category_id):
    """
    retrieving category products.
    """
    category = categories[category_id - 1]['id'].strip('en:')
    url = 'https://fr.openfoodfacts.org/cgi/search.pl'
    payload = {'json' :1,
               'action': 'process',
               'page_size': 40,
               'tagtype_0': 'categories',
               'tag_contains_0': 'contains',
               'tag_0': category,
              }
    response = requests.get(url, params=payload)
    res_json = response.json()
    products = res_json['products']

    return products
    

def main():
    categories = get_categories()
    products = get_category_products(categories, 1)


if __name__=='__main__':
    main()
