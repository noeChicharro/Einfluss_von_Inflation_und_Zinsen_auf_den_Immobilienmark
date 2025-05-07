import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('mysql+mysqlconnector://root:Wuschtel5!@localhost/bina', echo=False)

data = pd.read_csv('data/dataHive.csv') ## nicht der originale Name
print(data.head())

cursor = engine.raw_connection().cursor()

cursor.execute('DROP TABLE IF EXISTS dataHive')

## data_extraction_date,price_calculated,purchase_price,price_per_sqr_meter,room_count,bathroom_count,area_living,area_property,gwr_area_property,gwr_construction_year,gwr_floors,built_year,floor_number,transaction_type,property_category,property_type,zip,main_zip,canton,canton_name,latitude,longitude,geo_quality,min_price,max_price,initial_price


create_value_tabel = '''
CREATE TABLE dataHive (
    id INT AUTO_INCREMENT PRIMARY KEY,
    data_extraction_date DATE,
    price_calculated FLOAT,
    purchase_price FLOAT,
    price_per_sqr_meter FLOAT,
    room_count FLOAT,
    bathroom_count FLOAT,
    area_living FLOAT,
    area_property FLOAT,
    gwr_area_property FLOAT,
    gwr_construction_year FLOAT,
    gwr_floors FLOAT,
    built_year FLOAT,
    floor_number FLOAT,
    transaction_type VARCHAR(255),
    property_category VARCHAR(255),
    property_type VARCHAR(255),
    zip VARCHAR(255),
    main_zip VARCHAR(255),
    canton VARCHAR(255),
    canton_name VARCHAR(255),
    latitude FLOAT,
    longitude FLOAT,
    geo_quality FLOAT,
    min_price FLOAT,
    max_price FLOAT,
    initial_price FLOAT
)
'''

cursor.execute(create_value_tabel)
print('Table created')

data.to_sql('dataHive', con=engine, if_exists='append', index=False)
print('Data inserted into the database')

cursor.close()

