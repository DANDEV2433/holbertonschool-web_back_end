#!/usr/bin/env python3
"""
function that returns the list of school having a specific topic
"""

def schools_by_topic(mongo_collection, topic):
    """function that returns the list of school having a specific topic"""
    return list(mongo_collection.find({"topics": topic}))
