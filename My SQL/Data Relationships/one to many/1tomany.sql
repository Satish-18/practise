/*creating database*/
CREATE DATABASE shop;

/*showing database*/
show databases;

/*Using specific database for the work*/
use shop;

/*creating tables for the customers*/
create table customers(
id INT auto_increment primary key,
first_name VARCHAR(50),
last_name VARCHAR(50),
email VARCHAR(50)
);
 drop table customers;
/*inserting data into customers table*/
INSERT INTO customers (first_name, last_name, email) 
VALUES ('Boy', 'George', 'george@gmail.com'),
       ('George', 'Michael', 'gm@gmail.com'),
       ('David', 'Bowie', 'david@gmail.com'),
       ('Blue', 'Steele', 'blue@gmail.com'),
       ('Bette', 'Davis', 'bette@aol.com');

/*creating tables for the tables*/
create table orders(
id INT auto_increment primary key,
order_date DATE,
amount DECIMAL(8,3),
customer_id INT, foreign key(customer_id) references customers(id)
);

/*inserting data into orders table*/
INSERT INTO orders (order_date, amount, customer_id)
VALUES ('2016/02/10', 99.99, 1),
       ('2017/11/11', 35.50, 1),
       ('2014/12/12', 800.67, 2),
       ('2015/01/03', 12.50, 2),
       ('1999/04/11', 450.25, 5);
       
/*CROSS JOINT WWHICH IS ABSOLUTELY CREZZY*/
SELECT * FROM customers,orders;

/*finding the order placed by the boy name george*/
SELECT * FROM orders WHERE customer_id =
    (
        SELECT id FROM customers
        WHERE last_name='George'
    );
/*its better to do a EXPLICIT join then IMPLICIT join*/
/*INNER JOINS WHICH IS VERY READEABLE*/
/*IMPLICIT inner join*/
SELECT * FROM customers, orders WHERE customers.id=orders.customer_id;
SELECT first_name,last_name,order_date,amount  FROM customers, orders WHERE customers.id=orders.customer_id;

/*EXPLICIT inner join*/
SELECT * FROM customers join  orders on customers.id=orders.customer_id;
SELECT first_name,last_name,order_date,amount  FROM customers join orders on customers.id=orders.customer_id;

/*finding the biggest spender from the table*/
SELECT first_name,last_name,order_date,sum(amount) as spent from customers join orders on
customers.id=orders.customer_id
group by orders.customer_id order by spent desc;

/*LEFT JOIN*/
SELECT * FROM customers LEFT join  orders on customers.id=orders.customer_id;
SELECT first_name,last_name,order_date,amount  FROM customers left join orders on customers.id=orders.customer_id;

/*RIGHT JOIN*/
