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

cursor = connection.cursor()

##cursor.execute('DROP TABLE IF EXISTS valueYear')

create_value_tabel = '''
CREATE TABLE IF NOT EXISTS mietpreisindex (
    id INT AUTO_INCREMENT PRIMARY KEY,
    jahr INT,
    basisdatum DATE,
    indexwert FLOAT
)
'''

cursor.execute(create_value_tabel)
print('Table created')

connection.commit()
cursor.close()

connection.close()