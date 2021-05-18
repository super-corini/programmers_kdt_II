CREATE DATABASE bicsubi;

use bicsubi;

CREATE TABLE weapon
(
	_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    stock INTEGER
);

INSERT INTO weapon (name, stock) VALUES('RPG-07', 1);