import pandas as pd
from sqlalchemy import create_engine

## todo: files missing you idiot :D

engine = create_engine('mysql+mysqlconnector://root:Wuschtel5!@localhost/bina', echo=False)

data = pd.read_csv('data/Bruttoinlandprodukt_pro_Kopf_1991-2023.csv')
print(data.head())

cursor = engine.raw_connection().cursor()

cursor.execute('DROP TABLE IF EXISTS bruttoinlandprodukt')

create_value_tabel = '''
CREATE TABLE IF NOT EXISTS bruttoinlandprodukt (
    id INT AUTO_INCREMENT PRIMARY KEY,
    jahr INT,
    bip_pro_Kopf_CHF_laufende_Preise FLOAT,
    veraenderung_VJ_laufende_Preise FLOAT,
    index1991_100_laufende_Preise FLOAT,    
    bip_pro_Kopf_Veraenderung_VJ_Preise_Vorjahr FLOAT,
    index1991_100_Preise_Vorjahr FLOAT
)
'''

cursor.execute(create_value_tabel)
print('Table bruttoinlandprodukt created')

data.to_sql('bruttoinlandprodukt', con=engine, if_exists='append', index=False)
print('Data inserted into bruttoinlandprodukt')

cursor.execute('DROP TABLE IF EXISTS dataHive')

create_value_tabel = '''
CREATE TABLE dataHive (
    id INT AUTO_INCREMENT PRIMARY KEY,
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
    initial_price FLOAT,
    activated DATE
)
'''

cursor.execute(create_value_tabel)
print('Table dataHive created')

data.to_sql('dataHive', con=engine, if_exists='append', index=False)
print('Data inserted into dataHive')

cursor.execute('DROP TABLE IF EXISTS inflationsrate')

create_value_tabel = '''
CREATE TABLE IF NOT EXISTS inflationsrate (
    id INT AUTO_INCREMENT PRIMARY KEY,
    jahr INT,
    lik FLOAT,
    hvpi FLOAT
)
'''

cursor.execute(create_value_tabel)
print('Table inflationsrate created')

data.to_sql('inflationsrate', con=engine, if_exists='append', index=False)
print('Data inserted into inflationsrate')

data = pd.read_csv('data/lik_1914_2024.csv', sep=';')

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


cursor.execute('DROP TABLE IF EXISTS wohneigentum')

create_value_tabel = '''
CREATE TABLE IF NOT EXISTS wohneigentum (
    id INT AUTO_INCREMENT PRIMARY KEY,
    quartal VARCHAR(10),
    jahr INT,
    total FLOAT,
    gemeindetyp_1 FLOAT,
    gemeindetyp_2 FLOAT,    
    gemeindetyp_3 FLOAT,
    gemeindetyp_4 FLOAT,
    gemeindetyp_5 FLOAT
)
'''

cursor.execute(create_value_tabel)
print('Table wohneigentum created')

data.to_sql('wohneigentum', con=engine, if_exists='append', index=False)
print('Data inserted into wohneigentum')

cursor.execute('DROP TABLE IF EXISTS haushaltseinkommen')

create_value_tabel = '''
CREATE TABLE IF NOT EXISTS haushaltseinkommen (
    id INT AUTO_INCREMENT PRIMARY KEY,
    Jahr INT,
    Einkommen_unselbstaendige_Erwerbstaetigkeit varchar(10),    
    Einkommen_selbstaendige_Erwerbstaetigkeit varchar(10),
    Renten_AHV_IV varchar(10),
    Renten_BVG varchar(10),
    Sozialleistungen_Taggelder varchar(10),
    Sozialversicherungsbeitraege varchar(10),
    Steuern varchar(10),
    Krankenkassen_Praemien_Grundversicherung varchar(10),
    Krankenkassen_Praemien_Zusatzversicherungen varchar(10),
    Uebrige_Versicherungspraemien varchar(10),
    Gebuehren varchar(10),
    Spenden_Geschenke_Einladungen varchar(10),
    Nahrungsmittel_alkoholfreie_Getraenke varchar(10),
    Alkoholische_Getraenke_Tabakwaren varchar(10),
    Gast_Beherbergungsstaetten varchar(10),
    Bekleidung_Schuhe varchar(10),
    Wohnen_Energie varchar(10),
    Wohnungseinrichtung_Haushaltsfuehrung varchar(10),
    Gesundheitsausgaben varchar(10),
    Verkehr varchar(10),
    Nachrichtenuebermittlung varchar(10),
    Unterhaltung_Erholung_Kultur varchar(10),
    Andere_Waren_Dienstleistungen varchar(10),
    Anzahl_Selbstaendigerwerbende varchar(10),
    Anzahl_Unselbstaendigerwerbende varchar(10),   
    Anzahl_Rentner varchar(10), 
    Anzahl_Personen_in_Ausbildung varchar(10),
    Anzahl_andere varchar(10),
    Anzahl_KinderU15J varchar(10),
    Anzahl_PersonenU5J varchar(10),
    Anzahl_Personen5bis14J varchar(10),
    Anzahl_Personen_15bis24J varchar(10),
    Anzahl_Personen25bis34 varchar(10),
    Anzahl_Personen35bis44J varchar(10),
    Anzahl_Personen45bis54J varchar(10),
    Anzahl_Personen55bis64J varchar(10),
    Anzahl_Personen65bis74J varchar(10),
    Anzahl_PersonenUE75J varchar(10),
    Anteil_Einpersonenhaushalte varchar(10),
    Anteil_Mieterhaushalte varchar(10),
    Anteil_Rentnerhaushalte varchar(10),
    Anteil_Haushalte_mit_mindestens_1Auto varchar(10),
    Anteil_Haushalte_mit_mindestens_1Velo varchar(10),
    Anteil_Haushalte_mit_mindestens_1Computer varchar(10),
    Anteil_Haushalte_mit_mindestens_1Mobiltelefon varchar(10),  
    Anteil_Haushalte_mit_mindestens_1Haustier varchar(10)
)
'''

cursor.execute(create_value_tabel)
print('Table haushaltseinkommen created')

data.to_sql('haushaltseinkommen', con=engine, if_exists='append', index=False)
print('Data inserted into haushaltseinkommen')

cursor.execute('DROP TABLE IF EXISTS hypozinssatz')

create_value_tabel = '''
CREATE TABLE IF NOT EXISTS hypozinssatz (
    id INT AUTO_INCREMENT PRIMARY KEY,
    jahr INT,
    monat INT,
    festhypo_mittelwert FLOAT,
    festhypo_median FLOAT,
    festhypo_anzahl_abschluesse FLOAT,    
    variabelhypo_mittelwert FLOAT,
    variabelhypo_median FLOAT,
    variabelhypo_anzahl_abschluesse FLOAT
)
'''

cursor.execute(create_value_tabel)
print('Table hypozinssatz created')

data.to_sql('hypozinssatz', con=engine, if_exists='append', index=False)
print('Data inserted into hypozinssatz')


cursor.close()
