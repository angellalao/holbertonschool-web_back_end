#!/usr/bin/env python3
"""a python function called 'list_all' """
from pymongo import MongoClient

def list_all(mongo_collection):
    """ lists all documents in a mongo_collection """
    new_list = []
    for docs in mongo_collection.find():
        new_list.append(docs)
    return new_list
