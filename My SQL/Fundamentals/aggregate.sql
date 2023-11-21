/*counting the no of books*/
select count(*) from books;

/*counting the unique numbers of author first name*/
select count(distinct author_fname) from books;
select count(*) from books where title like '%the%';


/*using GROUP BY*/
select title,author_fname,author_lname, count(*) from books group by author_fname,author_lname;

/*MIN AND MAX*/
/*used  to find the minimum number*/
select min(pages) from books;
SELECT MIN(released_year) FROM books;

/*used  to find the maximum number*/
select max(pages) from books;
SELECT MAX(released_year) FROM books;

/*subquaries to solve the min max problem*/
select title,pages from books where pages=(select max(pages) from books);
/*OR*/
SELECT title, pages FROM books ORDER BY pages ASC LIMIT 1;
 
SELECT title, pages FROM books ORDER BY pages DESC LIMIT 1;

/*using min & max with group by*/
/*find the each year author published their first book*/
select author_fname,author_lname,min(released_year) from books group by author_fname,author_lname;
SELECT
  CONCAT(author_fname, ' ', author_lname) AS author,
  MAX(pages) AS 'longest book'
FROM books
GROUP BY author_lname,
         author_fname;
         
 /*SUM FUNCTION*/
 select author_fname,author_lname,sum(pages) from  books group by author_fname,author_lname;
 
 /*AVERAGE FUNCTION*/
  select author_fname,author_lname,avg(pages) from  books group by author_fname,author_lname;
  
  /*EXERCISES*/
  /*print no of books in the database*/
  select count(*) from books;
  
  /*find how many books released in each year*/
  select released_year,count(*) from books group by released_year;
  
  /*print total no of books in stocks*/
  select sum(stock_quantity) from books;
  
  /*print average release year for each author*/
  select author_fname,author_lname,avg(released_year) from  books group by author_fname,author_lname;
  
  /*find full name  of author who wrote longest book*/
  select concat(author_fname,' ',author_lname) as fullnam from books  where pages=(select max(pages) from books);
  
  /*print no of books released in each year also average no of pages*/
  select released_year as year, avg(pages) as 'avg pages' ,count(*) as '#book' from books group by released_year;