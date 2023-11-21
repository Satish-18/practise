/*here i am working with the books data*/
show databases;
USE book_shop;

/*creating the table name books*/
CREATE TABLE books(
		book_id INT NOT NULL AUTO_INCREMENT,
		title VARCHAR(100),
		author_fname VARCHAR(100),
		author_lname VARCHAR(100),
		released_year INT,
		stock_quantity INT,
		pages INT,
		PRIMARY KEY(book_id)
	);
 DESC books;
INSERT INTO books (title, author_fname, author_lname, released_year, stock_quantity, pages)
VALUES
('The Namesake', 'Jhumpa', 'Lahiri', 2003, 32, 291),
('Norse Mythology', 'Neil', 'Gaiman',2016, 43, 304),
('American Gods', 'Neil', 'Gaiman', 2001, 12, 465),
('Interpreter of Maladies', 'Jhumpa', 'Lahiri', 1996, 97, 198),
('A Hologram for the King: A Novel', 'Dave', 'Eggers', 2012, 154, 352),
('The Circle', 'Dave', 'Eggers', 2013, 26, 504),
('The Amazing Adventures of Kavalier & Clay', 'Michael', 'Chabon', 2000, 68, 634),
('Just Kids', 'Patti', 'Smith', 2010, 55, 304),
('A Heartbreaking Work of Staggering Genius', 'Dave', 'Eggers', 2001, 104, 437),
('Coraline', 'Neil', 'Gaiman', 2003, 100, 208),
('What We Talk About When We Talk About Love: Stories', 'Raymond', 'Carver', 1981, 23, 176),
("Where I'm Calling From: Selected Stories", 'Raymond', 'Carver', 1989, 12, 526),
('White Noise', 'Don', 'DeLillo', 1985, 49, 320),
('Cannery Row', 'John', 'Steinbeck', 1945, 95, 181),
('Oblivion: Stories', 'David', 'Foster Wallace', 2004, 172, 329),
('Consider the Lobster', 'David', 'Foster Wallace', 2005, 92, 343),
('10% Happier', 'Dan', 'Harris', 2014, 29, 256), 
('fake_book', 'Freida', 'Harris', 2001, 287, 428),
('Lincoln In The Bardo', 'George', 'Saunders', 2017, 1000, 367);

select * from books;
SELECT title FROM books WHERE title LIKE '%the%';

/*concatinating the names */
SELECT author_fname AS first,author_lname AS last,CONCAT(author_fname,' ',author_lname) AS fullname from books;

/*substring on mysql it works just like slicing in python*/
SELECT SUBSTRING(title,1,10) AS short_title FROM books;

SELECT concat(SUBSTRING(title,1,10),'...') AS short_title FROM books;

/*Replacing the parts of the string*/
SELECT REPLACE('hello world','o','s') AS repla;

SELECT REPLACE(title,'e','3') AS repla FROM books;

/*Reversing the string*/
SELECT REVERSE('helo world');

/*WXCERCISES*/
/*reversing and uppercasing the sentence below*/
SELECT reverse(upper('why i am soo bad'));

/*replacing every space in the title with the ->*/
select replace(title, ' ','->') from books;

/*printing the title fname in forward and lname in backward*/
select author_fname AS forward,reverse(author_lname) AS backward from books;

/*printing the fname and lname of author all in caps*/
select concat(upper(author_fname), ' ',upper(author_lname)) as caps from books;

select concat(title,  ' was realesed in ', released_year) as heed from books;

/*print the book title and the length of each book title*/
select title as book ,char_length(title) as character_count from books;

/*printing the 10 character of title and lastname,firstname of the author also printing the quantity number in num in stocks*/
select concat(substring(title,1,10),'...') as reduce,
concat(author_lname, ',',author_fname) as naming,
concat(stock_quantity, ' ',' in stock') as quantity from books;

/*EXERCISE PART 2:*/
/*Print the titles that contains stories in it*/
select title from books where title like '%stories%';

/*Finding the longesrt book*/
select title, pages from books order by pages desc limit 1;

/*print a summary containing a title and a year, for the 3 recent years*/
select concat(title ,'-',released_year) as summary from books order by released_year desc limit 3;

/*prints all the books with a author last name  that contains space in it*/
select title,author_lname from books where author_lname like '% %';

/*find 3 books with title year lowest stock*/
select title,released_year,stock_quantity from books order by stock_quantity  limit 3;

/*print title and author last name sorted  by author lname and then  by title*/
select title,author_lname from books order by author_lname, title;

/*sort alphabetically and caps all also concatinate by my favborate aurthor is auther full name!*/
select concat(' MY FAVOURATE AUTHOR IS  ',upper(author_fname),upper( author_lname),  ' !') as yell from books order by author_fname;