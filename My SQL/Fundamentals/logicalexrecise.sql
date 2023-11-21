SHOW databases;
USE book_shop;
select * from books;

/*Printing  all the books written before 1980*/
select title,released_year from books where released_year<1980;

/*Print the books written by egger or chabon*/
select title, author_lname from books where author_lname='eggers' or author_lname='chabon';
/*OR*/
select title, author_lname from books where author_lname IN('eggers','chabon');

/*Print the books written by lahiri after 2000*/
select title, author_lname from books where author_lname='lahiri' && released_year>2000;

/*Print the books where page count is in between 100-200*/
select title,pages from books where pages between 100 and 200;

/*Print all books of author whose last name start with 'c' and 's'*/
select title,author_lname from books where author_lname  like 'c%' or author_lname like 's%';

/*Print if title contains stories ->short stories, if other novel*/
select title,
case when title like '%stories%' then 'short stories'
else 'novel'  end as 'type' from books; 

/*Print title  author last name and print no of books written in plural form*/
select  title,author_fname,author_lname,
case
when  count(*)=1 then '1, book'  else concat(count(*),' ' 'books')  end as 'count' from books group by author_fname,author_lname;




 