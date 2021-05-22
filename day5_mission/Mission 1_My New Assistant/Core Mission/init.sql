CREATE TABLE weapon(
	id INT NOT NULL AUTO_INCREMENT, 
	name VARCHAR(200),
	stock INT,
	PRIMARY KEY(id)
);

INSERT INTO weapon (name, stock) VALUES('AK-47', 2);
INSERT INTO weapon (name, stock) VALUES('TRG', 5);
INSERT INTO weapon (name, stock) VALUES('FAMAS', 1);

