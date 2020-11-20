import mysql.connector 
print("hii") 
mydb = mysql.connector.connect( 
  host="localhost", 
  user="root", 
  password="1234567890" 
) 
 
print(mydb) 

 

#2 
import mysql.connector 
conn = mysql.connector.connect( 
  host="localhost", 
  user="root", 
  password="1234567890" 
) 
cursor=conn.cursor() 
cursor.execute("SELECT DATABASE()") 
data = cursor.fetchone() 
print("Connection established to:",data) 
conn.close() 
 

#3 
import mysql.connector 
conn = mysql.connector.connect(host="localhost",user="root",password="1234567890") 
cursor=conn.cursor() 
cursor.execute("DROP database IF EXISTS Mydatabase") 
cursor.execute("create database Mydatabase") 
print("List of databases:") 
cursor.execute("Show databases") 
print(cursor.fetchall()) 
conn.close() 















14-10-2020
#1
import mysql.connector 
conn = mysql.connector.connect(host="localhost",user="root",password="1234567890",database="mydata") 
c=conn.cursor() 
 
 
c.execute("create table customers (name VARCHAR(255),address VARCHAR(255))") 
c.close() 

 

 
#2
import mysql.connector 
conn = mysql.connector.connect(host="localhost",user="root",password="1234567890",database="mydata") 
c=conn.cursor() 
c.execute("create table customers1 (name VARCHAR(255),address VARCHAR(255))") 
c.execute("show tables") 
print(c.fetchall()) 
c.execute("insert into customers(name,address) values(%s,%s)", ("Johny" ,"highway")) 
conn.commit() 
print(c.rowcount,"record nserted") 
c.close() 

 
 














19-10-2020
mycursor.execute(select * student) 

 

 

 

 
#1
import mysql.connector 
mydb=mysql.connector.connect(host="localhost",user="root",password="1234567890" ,database="db1") 
mycursor=mydb.cursor() 
mycursor.execute("select * from students where year='204'") 
print(mycursor.fetchall()) 
mydb.close() 

 
  
#2
import mysql.connector 

mydb = mysql.connector.connect( 

    host = "localhost", 

    user="root", 

    password="1234", 

    database="db1") 

cursor = mydb.cursor() 

s="CREATE TABLE book(bookid integer (4), title varchar (20), price float (5,2))" 

cursor.execute(s) 

  

 

 
#3
import mysql.connector 

mydb = mysql.connector.connect( 

    host = "localhost", 

    user="root", 

    password="1234", 

    database="db1") 

cur = mydb.cursor() 

s = "INSERT INTO book (bookid,title, price) VALUES (%s,%s,%s)" 

books=[(2,'PHP',135),(3,'JAVA8',450),(4,'HTML',200)] 

cur.executemany(s,books) 

mydb.commit() 

 

 

 
#4
import mysql.connector 

mydb = mysql.connector.connect( 

    host = "localhost", 

    user="root", 

    password="1234", 

    database="db1") 

cur = mydb.cursor() 

s="UPDATE book SET price=price+20 WHERE price>200" 

cur.execute(s) 

mydb.commit() 

 

 

 

  
#5
import mysql.connector 

mydb = mysql.connector.connect( 

    host = "localhost", 

    user="root", 

    password="1234", 

    database="db1") 

cur = mydb.cursor() 

s="DELETE FROM book WHERE title='PHP'" 

cur.execute(s) 

mydb.commit() 

 
