#!/usr/bin/env python3
""" mongo_operations.py """


def schools_by_topic(mongo_collection, topic):
    """ Retrieves schools from the specified MongoDB """
    documents = mongo_collection.find({"topics": topic})
    return list(documents)
