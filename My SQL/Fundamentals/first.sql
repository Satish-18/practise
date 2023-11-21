
show databases;
USE patan;
/*crating a table*/
CREATE TABLE cats(
  cat_id INT NOT NULL AUTO_INCREMENT, 
     name   VARCHAR(100), 
     breed  VARCHAR(100), 
     age    INT, 
     PRIMARY KEY (cat_id) 
  ); 
  
/*inserting the data into the table*/
INSERT INTO cats(name, breed, age) 
VALUES ('Ringo', 'Tabby', 4),
       ('Cindy', 'Maine Coon', 10),
       ('Dumbledore', 'Maine Coon', 11),
       ('Egg', 'Persian', 4),
       ('Misty', 'Tabby', 13),
       ('George Michael', 'Ragdoll', 9),
       ('Jackson', 'Sphynx', 7);

SELECT * FROM cats;

SELECT name , breed from cats;

SELECT cat_id from cats;

/*selecting particular data from the taable*/
SELECT * FROM cats WHERE cat_id=age;

/*giving as aliases to the columns*/
SELECT name AS 'cat name', breed AS 'kitty breed' FROM cats;

/*updating the data */
UPDATE cats SET breed='cutecat' WHERE breed='Tabby';

/*deleting the data from the database*/
DELETE FROM cats WHERE name ='egg';