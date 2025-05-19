import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('mysql+mysqlconnector://root:Wuschtel5!@localhost/bina', echo=False)

data = pd.read_csv('data/lik_1914_2024.csv', sep=';')
print(data.head())

cursor = engine.raw_connection().cursor()
cursor.execute('DROP TABLE IF EXISTS likBig')

create_value_tabel = '''
CREATE TABLE IF NOT EXISTS likBig (
    id INT AUTO_INCREMENT PRIMARY KEY,
    jahr INT,
    lik FLOAT
)
'''

cursor.execute(create_value_tabel)
print('Table created')

data.to_sql('likBig', con=engine, if_exists='append', index=False)
print('Data inserted into the database') 

cursor.close()
