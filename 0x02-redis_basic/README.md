# Redis Basics

This project involves learning and implementing basic operations in Redis using Python. Redis is an in-memory data structure store used as a database, cache, and message broker.

## Table of Contents
- [Resources](#resources)
- [Learning Objectives](#learning-objectives)
- [Requirements](#requirements)
- [Installation](#installation)
- [Tasks](#tasks)
  - [0. Writing strings to Redis](#0-writing-strings-to-redis)
  - [1. Reading from Redis and recovering original type](#1-reading-from-redis-and-recovering-original-type)
  - [2. Incrementing values](#2-incrementing-values)
  - [3. Storing lists](#3-storing-lists)
  - [4. Retrieving lists](#4-retrieving-lists)

## Resources
Read or watch:
- [Redis Crash Course Tutorial](https://example.com)
- [Redis commands](https://example.com)
- [Redis Python client](https://example.com)
- [How to Use Redis With Python](https://example.com)

## Learning Objectives
- Learn how to use Redis for basic operations
- Learn how to use Redis as a simple cache

## Requirements
- All files will be interpreted/compiled on Ubuntu 18.04 LTS using Python 3.7
- All files should end with a new line
- A `README.md` file, at the root of the folder of the project, is mandatory
- The first line of all your files should be exactly `#!/usr/bin/env python3`
- Your code should use the `pycodestyle` style (version 2.5)
- All your modules should have documentation
- All your classes should have documentation
- All your functions and methods should have documentation
- All your functions and coroutines must be type-annotated

## Installation
To install Redis on Ubuntu 18.04 and the Redis Python client:

```bash
$ sudo apt-get -y install redis-server
$ pip3 install redis
$ sed -i "s/bind .*/bind 127.0.0.1/g" /etc/redis/redis.conf

