-- new user should be replica_user, with the host name set to %
-- password can be whatever mycase is  sumaya
-- replica_user must have the appropriate permissions to replicate your primary MySQL server
-- holberton_user will need SELECT privileges on the mysql.user table

CREATE USER IF NOT EXISTS 'replica_user'@'%' IDENTIFIED BY 'sumaya';
GRANT REPLICATION SLAVE ON *.* TO 'replica_user'@'%';
SELECT user, Repl_slave_priv FROM mysql.user;
