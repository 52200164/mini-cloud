CREATE DATABASE IF NOT EXISTS minicloud;
USE minicloud;
CREATE TABLE IF NOT EXISTS notes(
 id INT AUTO_INCREMENT PRIMARY KEY,
 title VARCHAR(100)
);
INSERT INTO notes(title) VALUES ('Hello database!');

CREATE DATABASE IF NOT EXISTS studentdb;
USE studentdb;
CREATE TABLE IF NOT EXISTS students(
 id INT PRIMARY KEY AUTO_INCREMENT,
 name VARCHAR(100),
 major VARCHAR(50),
 gpa FLOAT
);
INSERT INTO students(name, major, gpa) VALUES
('Nguyen Van A', 'CNTT', 3.2),
('Tran Thi B', 'CNTT', 3.5);
