# 0x00. MySQL Advanced

## Description
This project is focused on advanced MySQL topics such as indexing, stored procedures, triggers, and views. It aims to deepen understanding and proficiency in writing optimized SQL queries and managing MySQL databases effectively.

## Concepts
- **Advanced SQL**

## Resources
- [MySQL cheatsheet](https://devhints.io/mysql)
- [MySQL Performance: How To Leverage MySQL Database Indexing](https://www.percona.com/blog/2012/06/04/how-to-optimize-mysql-indexes/)
- [Stored Procedure](https://dev.mysql.com/doc/refman/8.0/en/stored-programs-defining.html)
- [Triggers](https://dev.mysql.com/doc/refman/8.0/en/triggers.html)
- [Views](https://dev.mysql.com/doc/refman/8.0/en/create-view.html)
- [Functions and Operators](https://dev.mysql.com/doc/refman/8.0/en/functions.html)
- [Trigger Syntax and Examples](https://dev.mysql.com/doc/refman/8.0/en/trigger-syntax.html)
- [CREATE TABLE Statement](https://dev.mysql.com/doc/refman/8.0/en/create-table.html)
- [CREATE PROCEDURE and CREATE FUNCTION Statements](https://dev.mysql.com/doc/refman/8.0/en/create-procedure.html)
- [CREATE INDEX Statement](https://dev.mysql.com/doc/refman/8.0/en/create-index.html)
- [CREATE VIEW Statement](https://dev.mysql.com/doc/refman/8.0/en/create-view.html)

## Learning Objectives
By the end of this project, you should be able to:
- Create tables with constraints.
- Optimize queries by adding indexes.
- Implement stored procedures and functions in MySQL.
- Implement views in MySQL.
- Implement triggers in MySQL.

## Requirements
- All your files will be executed on Ubuntu 18.04 LTS using MySQL 5.7 (version 5.7.30).
- All your files should end with a new line.
- All your SQL queries should have a comment just before (i.e. syntax above).
- All your files should start by a comment describing the task.
- All SQL keywords should be in uppercase (SELECT, WHERE, etc.).
- A `README.md` file, at the root of the folder of the project, is mandatory.
- The length of your files will be tested using `wc`.

## More Info
### Comments for your SQL file
```sql
$ cat my_script.sql
-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;
$

