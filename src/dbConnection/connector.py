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

## Jahr,grossen_Agglomeration,mittelgrossen_Agglomeration,kleinen_Agglomeration,intermediaere Gemeinde,laendliche_Gemeinde,EFH_grossen_Agglomeration,EFH_mittelgrossen_Agglomeration,EFH_kleinen_Agglomeration,EFH__Intermediaere_Gemeinde,EFH_Gemeinde,EGW_grossen_Agglomeration,EFH_mittelgrossen_Agglomeration,EGW_kleinen_Agglomeration,EGW_Intermediaere_Gemeinde,EGW_Laendliche_Gemeinde


cursor.execute(create_value_tabel)
print('Table created')

connection.commit()
cursor.close()

connection.close()