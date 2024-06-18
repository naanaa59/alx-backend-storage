#!/usr/bin/env python3
""" inserts a new document in a collection """


def insert_school(mongo_collection, **kwargs):
    """ inserts a new doc"""
    inserted = mongo_collection.insert_one(kwargs)
    return inserted.inserted_id
