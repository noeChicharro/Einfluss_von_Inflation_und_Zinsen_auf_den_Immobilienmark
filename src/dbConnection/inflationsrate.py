import mysql.connector
import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('mysql+mysqlconnector://root:Wuschtel5!@localhost/bina', echo=False)

data = pd.read_csv('../../data/inflationsrate_schweiz-2013-2023.csv')
print(data.head())

cursor = engine.raw_connection().cursor()

create_value_tabel = '''
CREATE TABLE IF NOT EXISTS inflationsrate (
    id INT AUTO_INCREMENT PRIMARY KEY,
    jahr INT,
    lik FLOAT,
    hvpi FLOAT
)
'''

cursor.execute(create_value_tabel)
print('Table created')

data.to_sql('inflationsrate', con=engine, if_exists='append', index=False)
print('Data inserted into the database')

cursor.close()
