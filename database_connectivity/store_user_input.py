import mysql.connector

conn = mysql.connector.connect(host='localhost', username='root', password='Dharm3059@',database='users')

cursor = conn.cursor()

query1 = 'create database USERS'
# cursor.execute(query1)

# cursor.execute('create table userdetails(rollno INT, name varchar(255), marks INT)')

rollno = int(input('Enter your Roll Number: '))
name = input('Enter your Name: ')
marks = float(input('Enter your Marks: '))

insert='insert into userdetails(rollno, name, marks) values(%s, %s, %s)'
values= (rollno, name, marks)

cursor.execute(insert,values)



conn.commit()
conn.close()

