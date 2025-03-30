import mysql.connector
import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('mysql+mysqlconnector://root:Wuschtel5!@localhost/bina', echo=False)

data = pd.read_csv('../../../data/landesindex_der_konsumentenpreise_wohnungsmiete_jahresdurchschnitte_1940_2024.csv')

data['basisdatum'] = data['basisdatum'].str.replace('00:00:00', '')
data['basisdatum'] = data['basisdatum'].str.replace(r'\s+', '')
##pd.to_csv(data)

##data.to_sql('mietpreisindex', con=engine, if_exists='append', index=False)
print('Data inserted into the database')

