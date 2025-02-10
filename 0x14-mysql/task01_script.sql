-- Create user holberton_user and grant permissions
CREATE USER holberton_user@localhost IDENTIFIED BY 'projectcorrection280hbtn';
GRANT REPLICATION CLIENT ON *.* TO 'holberton_user'@'localhost';
