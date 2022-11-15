/*non-coded comments on SQL*/

SHOW DATABASES;

CREATE DATABASE TTA;

USE TTA;

CREATE TABLE Studentscoring(
  ID int (10),
  Student varchar (25),
  Score int (10),
  Age int (10),
  PRIMARY KEY (ID)
);

EXPLAIN Studentscoring;

-- Student activity to create a table

 INSERT INTO Studentscoring
	(ID, Student, Score, Age)
VALUES (1, 'Chris',78, 23),
		(2, 'Charlotte',92, 22),
		(3, 'Caleb',92, 24),
		(4, 'Chantelle',88, 23);


SELECT *
FROM Studentscoring;

-- Student activity to insert data

SELECT Score
FROM Studentscoring;

SELECT Score, Age
FROM Studentscoring; 

SELECT Score
FROM Studentscoring 
WHERE Score >78;

SELECT *
FROM Studentscoring
WHERE Score>88 or Age>23;

UPDATE Studentscoring
SET Score=90
WHERE Student="Charlotte";

SELECT *
FROM Studentscoring;

UPDATE Studentscoring
SET Score=89, Age=21
WHERE Student="Caleb";

SELECT *
FROM Studentscoring

DELETE FROM Studentscoring
WHERE Student="Caleb";

SELECT *
FROM Studentscoring

ALTER TABLE Studentscoring
ADD Country varchar(25);

ALTER TABLE Studentscoring
MODIFY COLUMN Student varchar (25) NOT NULL;

EXPLAIN Studentscoring;

ALTER TABLE Studentscoring
DROP Age;

SELECT * FROM Studentscoring 
ORDER BY Score DESC;

SELECT * FROM Studentscoring
ORDER BY Student ;

SELECT Score, (SUM(Score)/COUNT(Score)) AS AverageScore
FROM  Studentscoring;

SELECT MIN (Score)
FROM Studentscoring;

SELECT MAX (Score)
FROM Studentscoring;

SELECT MIN (Score) AS Lowest
FROM Studentscoring;

SELECT COUNT (Score)
FROM Studentscoring;

SELECT SUM (Score)
FROM Studentscoring;

SELECT AVG (Score)
FROM Studentscoring;

SELECT COUNT (*)
FROM Studentscoring
WHERE Score>78;

-- Student activity to manipulate data