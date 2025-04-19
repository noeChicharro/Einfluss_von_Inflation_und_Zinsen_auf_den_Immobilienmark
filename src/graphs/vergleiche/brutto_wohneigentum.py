from sqlalchemy import create_engine
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import matplotlib.pyplot as matplot

engine = create_engine('mysql+mysqlconnector://root:Wuschtel5!@localhost/bina', echo=False)
cursor = engine.raw_connection().cursor()

selectWohn = """
    SELECT jahr, quartal, total
    FROM wohneigentum
"""

selectBrutto = """
    SELECT jahr, bip_pro_Kopf_CHF_laufende_Preise
    FROM bruttoinlandprodukt
"""
cursor.execute(selectWohn)
cursor.execute(selectBrutto)
cursor.close()

dfWohn = pd.read_sql(selectWohn, engine)
dfBrutto = pd.read_sql(selectBrutto, engine)
dfWohn = dfWohn.groupby('jahr')['total'].mean().reset_index()
print(dfWohn.head(), dfBrutto.head())
engine.dispose()

df_merged = pd.merge(dfWohn.groupby('jahr')['total'].mean().reset_index(), dfBrutto, on='jahr')
df_merged = df_merged.sort_values('jahr') 
print(df_merged.head())

plt.figure(figsize=(12, 6))

plt.barh(df_merged['jahr'], df_merged['total'], color='steelblue', label='Wohneigentum')

plt.barh(df_merged['jahr'], -df_merged['bip_pro_Kopf_CHF_laufende_Preise'], color='salmon', label='BIP pro Kopf')

plt.axvline(0, color='black')  # central vertical line
plt.xlabel('Wert')
plt.ylabel('Jahr')
plt.title('Vergleich Wohneigentum und BIP pro Kopf')
plt.legend()
plt.tight_layout()
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.show()