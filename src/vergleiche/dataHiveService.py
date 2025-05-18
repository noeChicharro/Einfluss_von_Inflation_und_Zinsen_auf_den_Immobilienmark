import dataService as dataService
import pandas as pd


selectDataHive = """
    SELECT * FROM dataHive
"""

dfDataHive = pd.read_sql(selectDataHive, dataService.engine)

dataService.engine.dispose()

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

dfDataHiveCleaned = dfDataHive[dfDataHive['purchase_price'] <= upper_bound].copy()

dfDataHiveCleaned['activated'] = pd.to_datetime(dfDataHiveCleaned['activated'], errors='coerce')

dfDataHiveCleaned['jahr'] = dfDataHiveCleaned['activated'].dt.year
dfDataHiveCleaned['monat'] = dfDataHiveCleaned['activated'].dt.to_period('M').astype(str)
dfDataHiveCleaned['quartal'] = dfDataHiveCleaned['activated'].dt.to_period('Q').astype(str)

# Gruppieren
monthly_median = dfDataHiveCleaned.groupby('monat')['purchase_price'].median()
quarterly_median = dfDataHiveCleaned.groupby('quartal')['purchase_price'].median()
yearly_median = dfDataHiveCleaned.groupby('jahr')['purchase_price'].median()

dfDataHiveCleaned['jahr'] = dfDataHiveCleaned['activated'].dt.year
dfDataHiveCleaned['monat'] = dfDataHiveCleaned['activated'].dt.month

monthly_prices = dfDataHiveCleaned.groupby(['jahr', 'monat'])['purchase_price'].median().reset_index()
monthly_prices.rename(columns={'purchase_price': 'median_kaufpreis'}, inplace=True)

monthly_prices = monthly_prices[(monthly_prices['jahr'] >= 2018) & (monthly_prices['jahr'] <= 2024)]
df_zins_filtered = dataService.dfHypo[(dataService.dfHypo['jahr'] >= 2018) & (dataService.dfHypo['jahr'] <= 2024)]

df_merge_zins = pd.merge(
    monthly_prices,
    df_zins_filtered,
    left_on=['jahr', 'monat'],
    right_on=['jahr', 'monat'],
    how='left'
)


yearly_prices = dfDataHiveCleaned[dfDataHiveCleaned['jahr'] <= 2023].groupby('jahr')['purchase_price'].median().reset_index()
yearly_prices.rename(columns={'purchase_price': 'median_kaufpreis'}, inplace=True)

dataService.dfLik = dataService.dfLik[['Jahr']].rename(columns={'Jahr': 'jahr'})

# Merge mit den Median-Kaufpreisen
df_merge_inflation = pd.merge(yearly_prices, dataService.dfLik, on='jahr', how='left')

# Neue Spalte 'quartal' erstellen (z. B. 1 für Jan–März, 2 für Apr–Juni etc.)
dfDataHiveCleaned['quartal'] = ((dfDataHiveCleaned['monat'] - 1) // 3 + 1)

# Median-Kaufpreis pro Jahr & Quartal berechnen
quarterly_prices = (
    dfDataHiveCleaned
    .groupby(['jahr', 'quartal'])['purchase_price']
    .median()
    .reset_index()
)

# Umbenennen für Klarheit
quarterly_prices.rename(columns={'purchase_price': 'median_kaufpreis'}, inplace=True)


# "q1", "q2", ... in 1, 2, ... umwandeln
dataService.dfWohn['quartal'] = dataService.dfWohn['quartal'].str.extract('(\d)').astype(int)

# Datentyp von 'quartal' auch in quarterly_prices sicherstellen
quarterly_prices['quartal'] = quarterly_prices['quartal'].astype(int)

# 🔗 Merge durchführen
df_merge_impi = pd.merge(
    quarterly_prices, dataService.dfWohn,
    on=['jahr', 'quartal'],
    how='left'
)
