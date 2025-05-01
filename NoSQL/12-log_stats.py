#!/usr/bin/env python3
"""
script that provides some stats about Nginx logs stored in MongoDB
"""
from pymongo import MongoClient


def log_stats():
    """
    script that provides some stats about Nginx logs stored in MongoDB
    """
    client = MongoClient()
    db = client.logs
    collection = db.nginx

    count = collection.count_documents({})
    print(f"{count} logs")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        count = collection.count_documents({"method": f"{method}"})
        print(f"\tmethod {method}: {count}")

    status_check = collection.count_documents(
        {"method": "GET", "path": "/status"}
        )
    print(f"{status_check} status check")

if __name__ == "__main__":
    log_stats()
