-- this script creates a database and table
-- creating a table hbtn_0d_usa with table states
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (
	id INT UNIQUE AUTO_INCREMENT,
	PRIMARY KEY (id),
	name VARCHAR(256) NOT NULL);
