# 0x01. NoSQL

This project covers MongoDB operations and PyMongo usage.

## Learning Objectives
- What NoSQL means
- What is difference between SQL and NoSQL
- What is ACID
- What is a document storage
- What are NoSQL types
- What are benefits of a NoSQL database
- How to query information from a NoSQL database
- How to insert/update/delete information from a NoSQL database
- How to use MongoDB

## Requirements

### MongoDB Command File
- All files interpreted on Ubuntu 18.04 LTS using MongoDB (version 4.2)
- All files should end with a new line
- First line should be a comment: `// my comment`
- File length tested using `wc`

### Python Scripts
- All files interpreted on Ubuntu 18.04 LTS using python3 (version 3.7) and PyMongo (version 3.10)
- All files should end with a new line
- First line should be exactly `#!/usr/bin/env python3`
- Code should use pycodestyle style (version 2.5.*)
- All modules and functions should have documentation
- Code should not be executed when imported

## Files

### MongoDB Commands
- `0-list_databases`: Lists all databases
- `1-use_or_create_database`: Creates or uses database my_db
- `2-insert`: Inserts document in school collection
- `3-all`: Lists all documents in school collection
- `4-match`: Lists documents with name="ALX"
- `5-count`: Counts documents in school collection
- `6-update`: Updates documents adding address attribute
- `7-delete`: Deletes documents with name="ALX School"
- `100-find`: Lists documents with name starting by "ALX" (Advanced)

### Python Scripts
- `8-all.py`: Lists all documents in a collection
- `9-insert_school.py`: Inserts a new document in a collection
- `10-update_topics.py`: Changes all topics of a school document
- `11-schools_by_topic.py`: Returns schools having a specific topic
- `12-log_stats.py`: Provides stats about Nginx logs
- `101-students.py`: Returns all students sorted by average score (Advanced)
- `102-log_stats.py`: Enhanced log stats with top 10 IPs (Advanced)
