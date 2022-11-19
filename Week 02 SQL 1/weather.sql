--shows a list of available databases

SHOW DATABASES;

--create a new database called "earth"

CREATE DATABASE EARTH;

--selects the table

USE EARTH;

--create a new table

CREATE TABLE EARTH_Weather(
  Country VARCHAR (25),
  City VARCHAR (25),
  Average_Annual_Max_Temp_C int (5),
  Average_Annual_Min_Temp_C int (5),
  Average_Annual_Sunhours int (5),
  Average_Highest_Percentage_Of_Sunshine_ int (3),
  Average_Lowest_Percentage_Of_Sunshine_ int (3),
  Average_Annual_Precipitation_mm int (5),
  Average_Annual_Rainy_Days int (5),
  Average_Annual_Humidity int (5),
  Average_Most_Windspeed VARCHAR (25),
  Average_Least_Windspeed VARCHAR (25),
  PRIMARY KEY (Country)
);

--view and shows the table structure 

EXPLAIN EARTH_Weather;

--inserts data into the table

INSERT INTO EARTH_Weather
    (Country, City, Average_Annual_Max_Temp_C, Average_Annual_Min_Temp_C, Average_Annual_Sunhours, Average_Highest_Percentage_Of_Sunshine_, Average_Lowest_Percentage_Of_Sunshine_, Average_Annual_Precipitation_mm, Average_Annual_Rainy_Days, Average_Annual_Humidity, Average_Most_Windspeed, Average_Least_Windspeed)
VALUES ('Enland', 'London', 16, 8, 1658, 45 ,21, 622, 111, 21, 'January', 'August'),
('Algeria', 'Algeiers', 24, 12, 2780, 79, 45, 598, 91, 67, 'December', 'August'),
('Morocco', 'Rabat', 22 ,13, 2920, 74, 57, 560, 76, 80, 'April', 'August'),
('Japan', 'Tokyo', 20, 12, 1930, 57, 28, 1602, 117, 64, 'September', 'September'),
('South-Korea', 'Seoul', 18, 9, 2133, 59, 27, 1428, 111, 60, 'April', 'September'),
('France', 'Paris', 16, 9, 1735, 49, 22, 630, 113, 78, 'January', 'August'),
('Germany', 'Berlin', 14, 5, 1712, 48, 20, 595, 103, 69, 'January', 'August');

--select and views the whole table with inserted data

SELECT *
FROM EARTH_Weather;

--selects the EARTH_Weather table then updates data france's data

UPDATE EARTH_Weather
SET Average_Annual_Min_Temp_C=8, Average_Least_Windspeed="February"
WHERE Country="France";

--selects the whole table to show the changes

SELECT *
FROM EARTH_Weather;

--deletes all data of France from the table

DELETE FROM EARTH_Weather
WHERE Country="France";

--selects and presents the whole EARTH_Weather table

SELECT *
FROM EARTH_Weather;