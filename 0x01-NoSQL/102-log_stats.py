#!/usr/bin/env python3
"""
Script that provides stats about Nginx logs with top 10 IPs
"""

from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs
    collection = db.nginx
    
    # Count total logs
    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")
    
    # Count methods
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")
    
    # Count status check
    status_check = collection.count_documents({
        "method": "GET",
        "path": "/status"
    })
    print(f"{status_check} status check")
    
    # Top 10 IPs
    pipeline = [
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ]
    
    top_ips = list(collection.aggregate(pipeline))
    print("IPs:")
    for ip_data in top_ips:
        print(f"\t{ip_data['_id']}: {ip_data['count']}")
