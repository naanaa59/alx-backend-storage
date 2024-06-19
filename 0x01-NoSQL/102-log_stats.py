#!/usr/bin/env python3
""" provides some stats about Nginx logs stored in MongoDB"""


from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx

    print("{} logs".format(nginx_collection.count_documents({})))
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        print("\tmethod {}: {}".format(
            method, nginx_collection.count_documents(
                {"method": method})))
    print("{} status check".format(nginx_collection.count_documents(
        {"method": "GET", "path": "/status"})))
    print("IPs:")
    pipeline = [
            {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
            {"$sort": {"count": -1}},
            {"$limit": 10}
    ]
    ips = nginx_collection.aggregate(pipeline)
    for ip in ips:
        print("\t{}: {}".format(ip['_id'], ip['count']))
