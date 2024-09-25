#Imports
import pytest

from fetch_key import FetchKey
from get_store_object import StoreObject
from parser import parser
from data_cleaner import clean_data

# Test data to verify functionalities in modules
test_list = ['Per förp. SPARA 9:00! ARVID NORDQUIST • 500g Flera olika sorter • Gäller ej hela bönor samt ekologisk • Jämförpris 109:80 kr/kg.',
             'Per förp. SPARA 9:00! ARVID NORDQUIST • 500g Flera olika sorter • Gäller ej hela bönor samt ekologisk • Jämförpris 109:80 kr/kg.',
             'Per förp. SPARA 9:00. ARVID NORDQUIST • 500g Flera olika sorter • Gäller ej hela bönor samt ekologisk • Jämförpris 109:80 kr/kg.']
test_dict = {'validity': ['2024-09-29T22:00:00.000Z','2024-09-29T22:00:00.000Z','2024-09-29T22:00:00.000Z'], 
            'name': ['KAFFE','KAFFE','KAFFE'],
            'price': [54.9, 54.9, 54.9],
            'unit': [],
            'save': [],
            'brand': [],
            }

#test_parsed_dict is used in two separate tests below
test_parsed_dict = parser(test_list, test_dict)

def test_store_object():
    """test access to key"""
    assert issubclass(StoreObject, FetchKey) == True
    test_object = StoreObject('test_store_name')
    assert type(test_object.headers['X-Api-Key']) == str

def test_parser():
    """test dimensions after parsing and one parse method"""
    assert len(test_parsed_dict['brand']) == len(test_parsed_dict['price'])
    assert test_parsed_dict['brand'][0] == 'NORDQUIST •'

def test_clean_data():
    """test removal of duplicates, cleaning of strings and conversion"""
    test_cleaned_dict = clean_data(test_parsed_dict)
    assert len(test_cleaned_dict['brand']) == 1
    assert test_cleaned_dict['brand'][0] == 'NORDQUIST'
    assert type(test_cleaned_dict['save'][0]) == float
    