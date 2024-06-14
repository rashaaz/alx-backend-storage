# 0x01. NoSQL

## Description
This project focuses on NoSQL databases, specifically MongoDB. You will learn the fundamentals of NoSQL, how it differs from SQL databases, and how to perform basic operations using MongoDB.

## Learning Objectives
By the end of this project, you should be able to:
- Explain what NoSQL means.
- Understand the difference between SQL and NoSQL.
- Define ACID properties.
- Explain document storage.
- Identify different types of NoSQL databases.
- Discuss the benefits of NoSQL databases.
- Query information from a NoSQL database.
- Insert, update, and delete information in a NoSQL database.
- Use MongoDB effectively.

## Resources
Read or watch:
- [NoSQL Databases Explained](https://www.youtube.com/watch?v=1ovFqT2KylE)
- [What is NoSQL?](https://www.mongodb.com/nosql-explained)
- [MongoDB with Python Crash Course - Tutorial for Beginners](https://www.youtube.com/watch?v=E-1xI85Zog8)
- [MongoDB Tutorial 2 : Insert, Update, Remove, Query](https://www.youtube.com/watch?v=FHA8hCkuYXI)
- [Aggregation](https://www.mongodb.com/docs/manual/aggregation/)
- [Introduction to MongoDB and Python](https://www.mongodb.com/compatibility/python)
- [mongo Shell Methods](https://www.mongodb.com/docs/manual/reference/method/)
- [Mongosh](https://www.mongodb.com/docs/mongodb-shell/)

## Requirements
### MongoDB Command Files
- All files will be interpreted/compiled on Ubuntu 18.04 LTS using MongoDB (version 4.2).
- Files should end with a new line.
- The first line of all files should be a comment: `// my comment`.
- A `README.md` file at the root of the folder is mandatory.
- The length of files will be tested using `wc`.

### Python Scripts
- All files will be interpreted/compiled on Ubuntu 18.04 LTS using Python 3.7 and PyMongo 3.10.
- Files should end with a new line.
- The first line of all files should be `#!/usr/bin/env python3`.
- A `README.md` file at the root of the folder is mandatory.
- Code should use the `pycodestyle` style (version 2.5.*).
- The length of files will be tested using `wc`.
- All modules should have documentation.
- All functions should have documentation.
- Code should not be executed when imported (use `if __name__ == "__main__":`).

## Installation
### Install MongoDB 4.2 on Ubuntu 18.04
```sh
$ wget -qO - https://www.mongodb.org/static/pgp/server-4.2.asc | sudo apt-key add -
$ echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.2 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.2.list
$ sudo apt-get update
$ sudo apt-get install -y mongodb-org
$ sudo service mongod start
$ mongo --version

