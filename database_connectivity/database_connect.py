import mysql.connector

# if you found error after write this line then you have to run this command: 
#    'pip install mysql-connector-python'

conn= mysql.connector.connect(host='localhost',username='root',password='Dharm3059@')

cursor=conn.cursor() # to create cursor

query1= 'CREATE DATABASE database1'
query2='SHOW DATABASES'

# cursor.execute(query1)
cursor.execute(query2)

#to print database name in vs code
# for name in cursor:
#     print(name)
    
# if you want to print in list
print(cursor.fetchall())
# -------------------------------------------------------------------------------------
# if you want to connect already exist database with python 

# conn= mysql.connector.connect(host='localhost',username='root',password='Dharm3059@', database='database1')

# cursor=conn.cursor()

# # query="CREATE TABLE dharm(name VARCHAR(255), age INT)"
# # query4 = 'INSERT INTO dharm(name,age) VALUES (%s,%s)'

# # values = [('dharmpatel', 21),]
# # cursor.execute(query4, values)  # for execute one

# values = [
#     ('dharmpatel', 21),
#     ('dharmpatel1', 22),
#     ('dharmpatel2', 23),
#     ('dharmpatel3', 24)
# ]
# # cursor.executemany(query4, values) # for execute many

# # to print table name in vs code
# query = 'SELECT * FROM dharm'
# cursor.execute(query)
# # for row in cursor:
# #     print(row)

# # if you want to print in list
# print(cursor.fetchall())


conn.commit()
conn.close()


# query4= 'INSERT INTO tableone(name,age) VALUES (%s,%s)' # %s is placeholder
# values=('dharm',21)
# cursor.execute(query4,values)
