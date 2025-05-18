from sqlalchemy import create_engine
import pandas as pd

engine = create_engine('mysql+mysqlconnector://root:Wuschtel5!@localhost/bina', echo=False)
cursor = engine.raw_connection().cursor()

# Inflationsrate
selectLik = """
    SELECT Jahr, lik, hvpi
    FROM inflationsrate
"""

# Wohneigentum
selectWohn = """
    SELECT jahr, quartal, total, gemeindetyp_1, gemeindetyp_2, gemeindetyp_3, gemeindetyp_4, gemeindetyp_5
    FROM wohneigentum
"""

# Haushaltseinkommen
selectEinkommen = """
    SELECT Jahr, Einkommen_unselbstaendige_Erwerbstaetigkeit
    FROM haushaltseinkommen
"""

# Bruttoinlandprodukt
selectBrutto = """
    SELECT jahr, bip_pro_Kopf_CHF_laufende_Preise
    FROM bruttoinlandprodukt
"""

# Hypothekenzinssatz
selectHypo = """
    SELECT jahr, monat, festhypo_mittelwert
    FROM hypozinssatz
"""

# DataHive
selectDataHive = """
    SELECT price_calculated, purchase_price, price_per_sqr_meter, room_count, bathroom_count, area_living, area_property, gwr_area_property, gwr_construction_year,
    gwr_floors, built_year, floor_number, transaction_type, property_category, property_type, zip, main_zip, canton, canton_name, latitude, longitude, geo_quality, min_price, max_price, initial_price
    FROM dataHive
"""

cursor.execute(selectLik)
cursor.execute(selectWohn)
cursor.execute(selectEinkommen)
cursor.execute(selectBrutto)
cursor.execute(selectHypo)
cursor.execute(selectDataHive)
cursor.close()

dfLik = pd.read_sql(selectLik, engine)
dfWohn = pd.read_sql(selectWohn, engine)
dfEinkommen = pd.read_sql(selectEinkommen, engine)
dfBrutto = pd.read_sql(selectBrutto, engine)
dfHypo = pd.read_sql(selectHypo, engine)
dfDataHive = pd.read_sql(selectDataHive, engine)



## Strings zu numerischen Werten umwandeln
dfEinkommen['Einkommen_unselbstaendige_Erwerbstaetigkeit'] = (
    dfEinkommen['Einkommen_unselbstaendige_Erwerbstaetigkeit']
    .str.replace("'", '', regex=False)    
    .str.replace(",", '.', regex=False)    
    .str.replace(" ", '', regex=False)    
)
dfEinkommen['Einkommen_unselbstaendige_Erwerbstaetigkeit'] = pd.to_numeric(dfEinkommen['Einkommen_unselbstaendige_Erwerbstaetigkeit'], errors='coerce')


## Gemeindetypen Jahresdruchschnitt
## durchschnitt aller monatlichen/quartals werte
dfGemeinde1_yearly = dfWohn.groupby('jahr')['gemeindetyp_1'].mean().reset_index()
dfGemeinde2_yearly = dfWohn.groupby('jahr')['gemeindetyp_2'].mean().reset_index()
dfGemeinde3_yearly = dfWohn.groupby('jahr')['gemeindetyp_3'].mean().reset_index()
dfGemeinde4_yearly = dfWohn.groupby('jahr')['gemeindetyp_4'].mean().reset_index()
dfGemeinde5_yearly = dfWohn.groupby('jahr')['gemeindetyp_5'].mean().reset_index()

dfGemeindetypen = dfGemeinde1_yearly.copy()
dfGemeindetypen = dfGemeindetypen.rename(columns={'gemeindetyp_1': 'Typ 1'}) ## Städtische Gemeinde einer kleinen Agglomeration
dfGemeindetypen['Typ 2'] = dfGemeinde2_yearly['gemeindetyp_2'] ## Städtische Gemeinde einer mittelgrossen Agglomeration 
dfGemeindetypen['Typ 3'] = dfGemeinde3_yearly['gemeindetyp_3'] ## Städtische Gemeinde einer kleinen oder ausserhalb einer Agglomeration 
dfGemeindetypen['Typ 4'] = dfGemeinde4_yearly['gemeindetyp_4'] ## Intermediäre Gemeinde 
dfGemeindetypen['Typ 5'] = dfGemeinde5_yearly['gemeindetyp_5'] ## Ländliche Gemeinde 
 
## Jährlicher Hypothekenzinssatz (Durchschnitt)
dfHypo_yearly = dfHypo.groupby('jahr')['festhypo_mittelwert'].mean().reset_index()

## Jährliches Wohneigentum (Durchschnitt)
dfWohn_yearly = dfWohn.groupby('jahr')['total'].mean().reset_index()

## Common Hypothekenzinssatz und Wohneigentum (jährlich)
dfCommonHypoWohn = pd.merge(dfHypo_yearly, dfWohn_yearly, on='jahr')
dfCommonHypoWohn = dfCommonHypoWohn.sort_values('jahr')

## Common Einkommen und Wohneigentum (jährlich)
dfEinkommen.rename(columns={'Jahr': 'jahr'}, inplace=True)
dfWohn = dfWohn[dfWohn['jahr'] >= 2017]
dfEinkommen = dfEinkommen[dfEinkommen['jahr'].isin(dfWohn['jahr'])]
dfCommonWohnEinkommen = pd.merge(dfWohn, dfEinkommen, on='jahr')
dfCommonWohnEinkommen = dfCommonWohnEinkommen.sort_values('jahr')

## Common Wohneigentum und BIP (jährlich)
dfCommonBipWohn = pd.merge(dfWohn.groupby('jahr')['total'].mean().reset_index(), dfBrutto, on='jahr')
dfCommonBipWohn = dfCommonBipWohn.sort_values('jahr') 

## Common Einkommen und BIP (jährlich)
dfEinkommen.rename(columns={'Jahr': 'jahr'}, inplace=True)
dfBrutto = dfBrutto[dfBrutto['jahr'] >= 2017]
dfBrutto = dfBrutto[dfBrutto['jahr'].isin(dfBrutto['jahr'])]
dfCommonBipEinkommen = pd.merge(dfBrutto, dfEinkommen, on='jahr')

## DataHive 
price_columns = [
    "price_calculated", "purchase_price", "price_per_sqr_meter",
    "min_price", "max_price", "initial_price"
]
dfDataHivePrice = dfDataHive[price_columns].copy()
dfDataHiveOther = dfDataHive.drop(columns=price_columns).copy()


## Toni sachen
df_zins = pd.read_sql("SELECT * FROM hypozinssatz", engine)
df_inflation = pd.read_sql("SELECT * FROM inflationsrate", engine)
df_wohn = pd.read_sql("SELECT * FROM wohneigentum", engine)
df_arbeitslos = pd.read_sql("SELECT * FROM erwerbslosenquote", engine)

# SQL-Query definieren
selectDataHive = "SELECT * FROM dataHive"
 
# Daten laden
dfDataHive = pd.read_sql(selectDataHive, engine)

engine.dispose()

# Quartile und IQR berechnen
q1 = dfDataHive['purchase_price'].quantile(0.25)
q3 = dfDataHive['purchase_price'].quantile(0.75)
iqr = q3 - q1

# Obere Grenze für Ausreisser definieren
upper_bound = q3 + 1.5 * iqr
print(f"Q1: {q1:,.0f} CHF")
print(f"Q3: {q3:,.0f} CHF")
print(f"IQR: {iqr:,.0f} CHF")
print(f"Obere Ausreissergrenze: {upper_bound:,.0f} CHF")

df_clean = dfDataHive[dfDataHive['purchase_price'] <= upper_bound].copy()

df_clean['activated'] = pd.to_datetime(df_clean['activated'], errors='coerce')

df_clean['year'] = df_clean['activated'].dt.year
df_clean['month'] = df_clean['activated'].dt.to_period('M').astype(str)
df_clean['quarter'] = df_clean['activated'].dt.to_period('Q').astype(str)

# Gruppieren
monthly_median = df_clean.groupby('month')['purchase_price'].median()
quarterly_median = df_clean.groupby('quarter')['purchase_price'].median()
yearly_median = df_clean.groupby('year')['purchase_price'].median()

df_clean['year'] = df_clean['activated'].dt.year
df_clean['month'] = df_clean['activated'].dt.month

monthly_prices = df_clean.groupby(['year', 'month'])['purchase_price'].median().reset_index()
monthly_prices.rename(columns={'purchase_price': 'median_kaufpreis'}, inplace=True)

monthly_prices = monthly_prices[(monthly_prices['year'] >= 2018) & (monthly_prices['year'] <= 2024)]
df_zins_filtered = df_zins[(df_zins['jahr'] >= 2018) & (df_zins['jahr'] <= 2024)]

df_merge_zins = pd.merge(
    monthly_prices,
    df_zins_filtered,
    left_on=['year', 'month'],
    right_on=['jahr', 'monat'],
    how='left'
)


yearly_prices = df_clean[df_clean['year'] <= 2023].groupby('year')['purchase_price'].median().reset_index()
yearly_prices.rename(columns={'purchase_price': 'median_kaufpreis'}, inplace=True)

df_lik = df_inflation[['jahr', 'lik']].rename(columns={'jahr': 'year', 'lik': 'inflation_lik'})

# Merge mit den Median-Kaufpreisen
df_merge_inflation = pd.merge(yearly_prices, df_lik, on='year', how='left')

# Neue Spalte 'quartal' erstellen (z. B. 1 für Jan–März, 2 für Apr–Juni etc.)
df_clean['quartal'] = ((df_clean['month'] - 1) // 3 + 1)

# Median-Kaufpreis pro Jahr & Quartal berechnen
quarterly_prices = (
    df_clean
    .groupby(['year', 'quartal'])['purchase_price']
    .median()
    .reset_index()
)

# Umbenennen für Klarheit
quarterly_prices.rename(columns={'purchase_price': 'median_kaufpreis'}, inplace=True)

df_impi = df_wohn[['jahr', 'quartal', 'total']].rename(
    columns={'jahr': 'year', 'quartal': 'quartal', 'total': 'impi_index'}
)

# "q1", "q2", ... in 1, 2, ... umwandeln
df_impi['quartal'] = df_impi['quartal'].str.extract('(\d)').astype(int)

# Datentyp von 'quartal' auch in quarterly_prices sicherstellen
quarterly_prices['quartal'] = quarterly_prices['quartal'].astype(int)

# 🔗 Merge durchführen
df_merge_impi = pd.merge(
    quarterly_prices, df_impi,
    on=['year', 'quartal'],
    how='left'
)
