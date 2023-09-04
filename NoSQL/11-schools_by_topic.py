#!/usr/bin/env python3
""" a python function called 'schools by topic' """


def schools_by_topic(mongo_collection, topic):
    """returns a list of objects/schools having a specific topic """
    query = {"topics": {"$elemMatch": {"$eq": topic}}}
    result = mongo_collection.find(query)
    return result
