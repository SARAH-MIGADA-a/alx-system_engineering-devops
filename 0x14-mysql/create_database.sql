-- Create a database named tyrell_corp
-- create a table named nexus6 and add at least one entry to it.
-- Make sure that holberton_user has SELECT permissions on your table

CREATE DATABASE IF NOT EXISTS tyrell_corp;
-- use the created database
USE tyrell_corp;
-- create table nexus6
CREATE TABLE IF NOT EXISTS nexus6 (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255)
);
-- Add at least one entry to the table, add a row to the table
INSERT INTO nexus6 (name) VALUES ('Leon');
-- Grant SELECT permissions to holberton_user
GRANT SELECT ON tyrell_corp.nexus6 TO 'holberton_user'@'localhost';
