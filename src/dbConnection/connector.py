import mysql.connector
from sqlalchemy import create_engine

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