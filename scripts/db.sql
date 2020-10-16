CREATE TABLE users (
	user_id integer PRIMARY KEY,
	first varchar(50),
	last varchar(50),
	age integer
);

CREATE TABLE employees (
	user_id integer PRIMARY KEY,
	first varchar(50),
	last varchar(50),
	email varchar(50),
	city varchar(50),
	age integer
);

INSERT INTO users(user_id, first, last, age)
VALUES (1, 'Martin', 'Toma', 27);

INSERT INTO users(user_id, first, last, age)
VALUES (2, 'Alice', 'Dawson', 43);

INSERT INTO users(user_id, first, last, age)
VALUES (3, 'Jenny', 'Watson', 38);

INSERT INTO employees(user_id, first, last, email, city, age)
VALUES (1, 'Tom', 'Qwerty', 'tom@qwerty.com', 'Monaco', 10);

INSERT INTO employees(user_id, first, last, email, city, age)
VALUES (2, 'Jerry', 'Zxcvb', 'jerry@zxcvb.com', 'Kuala Lumpur', 11);