#!/usr/bin/env python3
""" mongo_operations.py """


def list_all(mongo_collection):
    """ Retrieves all documents """
    documents = mongo_collection.find()

    if documents.count() == 0:
        return []

    return documents
