import mysql.connector

conn = mysql.connector.connect(host='localhost', username='root', password ='Dharm3059@',database='dharm1')

cursor = conn.cursor()

query1 = 'CREATE DATABASE dharm1'
# cursor.execute(query1)

query2 = 'CREATE TABLE table1(name VARCHAR(255),  age INT)'
# cursor.execute(query2)

query3 = "INSERT INTO table1 values('PATEL', 21)"
query4 = "INSERT INTO table1 values('DHARM',20)"
cursor.execute(query3)
cursor.execute(query4)

query5 = "INSERT INTO table1(name,age) VALUES (%s,%s) "
values = [('dhruv',30), 
          ('govind',35)]
cursor.executemany(query5,values)

conn.commit()
conn.close()