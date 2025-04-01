import mysql.connector

connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Wuschtel5!',
    database='bina'
)

if connection.is_connected():
    print('Connected to MySQL database')
else:
    print('Connection failed')  

connection.close()