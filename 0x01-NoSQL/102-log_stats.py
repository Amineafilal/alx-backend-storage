#!/usr/bin/env python3
"""
Script provides stats about Nginx logs stored in MongoDB,
including the top 10 most frequent IPs.
"""
from pymongo import MongoClient


def log_stats():
    """
    Provides stats about Nginx logs and the top 10 most present IPs.
    """
    client = MongoClient('mongodb://127.0.0.1:27017')
    collection = client.logs.nginx

    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")

    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    status_check = collection.count_documents(
        {"method": "GET", "path": "/status"}
    )
    print(f"{status_check} status check")

    print("IPs:")
    pipeline = [
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ]
    top_ips = collection.aggregate(pipeline)
    for ip in top_ips:
        print(f"\t{ip.get('_id')}: {ip.get('count')}")


if __name__ == "__main__":
    log_stats()
