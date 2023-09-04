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
    get = collection.count_documents({"method": "GET"})
    print(f"\tmethod GET: {get}")
    post = collection.count_documents({"method": "POST"})
    print(f"\tmethod POST: {post}")
    put = collection.count_documents({"method": "PUT"})
    print(f"\tmethod PUT: {put}")
    patch = collection.count_documents({"method": "PATCH"})
    print(f"\tmethod PATCH: {patch}")
    delete = collection.count_documents({"method": "DELETE"})
    print(f"\tmethod DELETE: {delete}")
    method_path = collection.count_documents(
        {"method": "GET", "path": "/status"})
    print(f"{method_path} status check")
