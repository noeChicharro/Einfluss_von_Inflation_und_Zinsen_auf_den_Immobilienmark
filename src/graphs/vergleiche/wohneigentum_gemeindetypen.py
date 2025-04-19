from sqlalchemy import create_engine
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import matplotlib.pyplot as matplot

engine = create_engine('mysql+mysqlconnector://root:Wuschtel5!@localhost/bina', echo=False)
cursor = engine.raw_connection().cursor()

selectWohn = """
    SELECT jahr, quartal, gemeindetyp_1, gemeindetyp_2, gemeindetyp_3, gemeindetyp_4, gemeindetyp_5
    FROM wohneigentum
"""

cursor.execute(selectWohn)
cursor.close()

dfWohn = pd.read_sql(selectWohn, engine)
print(dfWohn.head())
engine.dispose()

## durchschnitt aller monatlichen/quartals werte
dfGemeinde1_yearly = dfWohn.groupby('jahr')['gemeindetyp_1'].mean().reset_index()
dfGemeinde2_yearly = dfWohn.groupby('jahr')['gemeindetyp_2'].mean().reset_index()
dfGemeinde3_yearly = dfWohn.groupby('jahr')['gemeindetyp_3'].mean().reset_index()
dfGemeinde4_yearly = dfWohn.groupby('jahr')['gemeindetyp_4'].mean().reset_index()
dfGemeinde5_yearly = dfWohn.groupby('jahr')['gemeindetyp_5'].mean().reset_index()
print(dfGemeinde1_yearly.head())

df_all = dfGemeinde1_yearly.copy()
df_all = df_all.rename(columns={'gemeindetyp_1': 'Typ 1'}) ## Städtische Gemeinde einer kleinen Agglomeration
df_all['Typ 2'] = dfGemeinde2_yearly['gemeindetyp_2'] ## Städtische Gemeinde einer mittelgrossen Agglomeration 
df_all['Typ 3'] = dfGemeinde3_yearly['gemeindetyp_3'] ## Städtische Gemeinde einer kleinen oder ausserhalb einer Agglomeration 
df_all['Typ 4'] = dfGemeinde4_yearly['gemeindetyp_4'] ## Intermediäre Gemeinde 
df_all['Typ 5'] = dfGemeinde5_yearly['gemeindetyp_5'] ## Ländliche Gemeinde 

# Plot
plt.figure(figsize=(12, 6))

highlight = 'Typ 4' 

for col in ['Typ 1', 'Typ 2', 'Typ 3', 'Typ 4', 'Typ 5']:

   ## plt.plot(df_all['jahr'], df_all[col], marker='o', label=col) -> wenn nicht gehilighted werden soll diesen code verwenden und if auskommentieren
    if col == highlight:
        plt.plot(df_all['jahr'], df_all[col], label=col, linewidth=3, color='crimson')
    else:
        plt.plot(df_all['jahr'], df_all[col], label=col, linewidth=1.5, linestyle='--', color='gray')

plt.title('Entwicklung des Wohneigentums über die Jahre')
plt.xlabel('Jahr')
plt.ylabel('Durchschnittlicher Wert')
plt.legend(title='Gemeindetyp')
plt.grid(True)
plt.tight_layout()
plt.show()

highlight = 'Typ 3'

