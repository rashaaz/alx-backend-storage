#!/usr/bin/env python3
""" mongo_operations.py """


def update_topics(mongo_collection, name, topics):
    """ Updates documents in the specified """
    query = {"name": name}
    new_values = {"$set": {"topics": topics}}

    mongo_collection.update_many(query, new_values)
