#!/usr/bin/env python3
""" mongo_operations.py """


def insert_school(mongo_collection, **kwargs):
    """ Inserts a document into the specified MongoDB collection """
    return mongo_collection.insert(kwargs)
