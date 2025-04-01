import mysql.connector
import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('mysql+mysqlconnector://root:Wuschtel5!@localhost/bina', echo=False)

data = pd.read_csv('../../data/Landesindex der Konsumentenpreise_LIK 1914-2025.csv')
print(data.head())

pd_cleaned = pd.dropna()

cursor = engine.raw_connection().cursor()

create_value_tabel = '''
CREATE TABLE IF NOT EXISTS konsumentenpreise (
    id INT AUTO_INCREMENT PRIMARY KEY,
    Jahr INT,
    Basis_Datum DATE,
    Landesindex_der_Konsumentenpreise FLOAT
)
'''

cursor.execute(create_value_tabel)
print('Table created')

data.to_sql('konsumentenpreise', con=engine, if_exists='append', index=False)
print('Data inserted into the database')

cursor.close()
