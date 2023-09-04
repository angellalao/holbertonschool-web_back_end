#!/usr/bin/env python3
""" script that provides some stats about Nginx logs stored in MongoDB
database: logs, collection: nginx"""
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient("localhost", 27017)
    db = client.logs
    collection = db.nginx

    docs = collection.count_documents({})
    print(f"{docs} logs")
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        lower_str = method.lower()
        lower_str = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {lower_str}")

        method_path = collection.count_documents(
            {"method": "GET", "path": "/status"})
    print(f"{method_path} status check")
