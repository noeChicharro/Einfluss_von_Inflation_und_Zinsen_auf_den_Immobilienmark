import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('mysql+mysqlconnector://root:Wuschtel5!@localhost/bina', echo=False)

data = pd.read_csv('data/durchschnittsalter_kantone_2010-2023_longformat.csv')
print(data.head())

cursor = engine.raw_connection().cursor()

cursor.execute('DROP TABLE IF EXISTS durchschnittsalter')

create_value_tabel = '''
CREATE TABLE IF NOT EXISTS durchschnittsalter (
    id INT AUTO_INCREMENT PRIMARY KEY,
    kanton_kurz VARCHAR(10),
    kanton VARCHAR(50),
    durchschnittsalter FLOAT,
    jahr INT
)
'''

cursor.execute(create_value_tabel)
print('Table created')

data.to_sql('durchschnittsalter', con=engine, if_exists='append', index=False)
print('Data inserted into the database')

cursor.close()
