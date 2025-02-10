-- Task 1: Create user holberton_user and grant permissions
CREATE USER IF NOT EXISTS holberton_user@localhost IDENTIFIED BY 'projectcorrection280hbtn';
GRANT REPLICATION CLIENT ON *.* TO 'holberton_user'@'localhost';

-- Task 2: Create database tyrell_corp and its table nexus6
CREATE DATABASE IF NOT EXISTS tyrell_corp;
USE tyrell_corp;
CREATE TABLE IF NOT EXISTS nexus6(id INTEGER, name TEXT);

-- Check if "Jarvis" exists in the nexus6 table
INSERT INTO nexus6 (id, name)
SELECT 0, 'Jarvis'
FROM dual
WHERE NOT EXISTS (SELECT 1 FROM nexus6 WHERE name = 'Jarvis');

-- Grant select permission on table nexus6 to holberton_user
GRANT SELECT ON tyrell_corp.nexus6 TO holberton_user@localhost;

-- Task 3: Create user replica_user for replication
CREATE USER IF NOT EXISTS replica_user@'%' IDENTIFIED BY 'replica_user';
GRANT REPLICATION SLAVE ON *.* TO 'replica_user'@'%';

-- Grant select permission on mysql.user table to holberton_user
GRANT SELECT ON mysql.user TO holberton_user@localhost;

CREATE USER IF NOT EXISTS web02@'34.203.29.50' IDENTIFIED BY 'web02';
GRANT REPLICATION SLAVE ON *.* TO web02@'34.203.29.50';
