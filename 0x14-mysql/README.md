# Curriculum: SE Foundations - MySQL, DevOps, SysAdmin

# Project: 0x14. MySQL
## Overview

This project is part of the SE curriculum and focuses on MySQL installation, setup, and administration, as well as aspects of DevOps and SysAdmin tasks. It is designed to reinforce foundational skills in database administration, web stack debugging, and DevOps practices.

## Project Description
The project involves setting up a MySQL environment, configuring primary-replica replication, database backup strategy, and related tasks. I'll be working on tasks such as installing MySQL, setting up users and permissions, database creation, replication setup, and implementing a backup solution.

## Concepts Covered

- Fresh Reset and Install MySQL 5.7
- Database administration
- Web stack debugging
- Primary-replica cluster setup
- Database backup strategy

## Learning Objectives

By completing this project, I am expected to understand and be able to explain:

- The main role of a database
- Database replication and its purpose
- Importance of storing database backups in different physical locations
- Regular database backup strategy checks

## Tasks

### Task 0: Install MySQL
- Install MySQL 5.7.x on web-01 and web-02 servers.

### Task 1: Let Us In!
- Create a MySQL user `holberton_user` on both servers with appropriate permissions.

### Task 2: If Only You Could See What I've Seen with Your Eyes
- Create a database named `tyrell_corp` and a table named `nexus6` with entries on web-01.

### Task 3: Quite an Experience to Live in Fear, Isn't It?
- Create a user `replica_user` on web-01 for replication purposes.

### Task 4: Setup a Primary-Replica Infrastructure using MySQL
- Configure primary-replica setup with web-01 as primary and web-02 as replica.

### Task 5: MySQL Backup
- Write a Bash script to generate a MySQL dump, compress it, and create a backup.

## Resources

Read or watch:
- [What is a primary-replica cluster](https://www.digitalocean.com/community/tutorials/how-to-choose-a-redundancy-plan-to-ensure-high-availability#sql-replication)
- [MySQL primary replica setup](https://www.digitalocean.com/community/tutorials/how-to-set-up-replication-in-mysql)
- [Build a robust database backup strategy](https://www.databasejournal.com/ms-sql/developing-a-sql-server-backup-strategy/)

Man or help:
- `mysqldump`

---
