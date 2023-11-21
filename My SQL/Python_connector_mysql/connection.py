#creating the connection for the mysql
import mysql.connector
mydb = mysql.connector.connect(
	host = "localhost",
	user= " root",
	password = "mysql@9861351199",
	database = "testing",
	)

my_cursor = mydb.cursor()
#creating table
my_cursor.execute("CREATE TABLE users(username VARCHAR(20),email VARCHAR(20),age INTEGER ,user_id INTEGER AUTO_INCREMENT PRIMARY KEY)")
my_cursor.execute("SHOW TABLES")
for table in my_cursor:
	print(table)

#inserting single data into the database
data_stuff ="INSERT INTO users(username,email,age) VALUES(%s,%s,%s)"
data = ('satish','satish@gmail.com',20)
my_cursor.execute(data_stuff,data) 
mydb.commit()
 
#inserting multiple data into the the database
data_stuff ="INSERT INTO users(username,email,age) VALUES(%s,%s,%s)"
data = [
('hari','hari@gmail.com',25),
('shyam','shyam@gmail.com',30),
]
my_cursor.executemany(data_stuff,data)#
mydb.commit()

#selecting data from database
my_cursor.execute("SELECT * FROM users")
result = my_cursor.fetchall()
for row in result:
	print(row)