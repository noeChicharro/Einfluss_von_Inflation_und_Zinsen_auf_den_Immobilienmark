import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import sys
import os

# Parent directory für das Projekt hinzufügen
project_root = os.path.abspath("..")  
if project_root not in sys.path:
    sys.path.append(project_root)

# Imports aller verwendeten Module
# numpy
import numpy as np
# pandas
import pandas as pd
# matplotlib
import matplotlib.pyplot as matplot
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
# seaborn
import seaborn as sns
# sklearn
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_absolute_error, mean_squared_error
# statsmodels
from statsmodels.tsa.stattools import adfuller
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.statespace.sarimax import SARIMAX
from statsmodels.tsa.arima.model import ARIMA
# itertools
import itertools
# squarify
import squarify 

# Vorbereitete Daten aus Datenbank 
import dataService as dataService
import dataHiveService as dhService

import importlib
importlib.reload(dataService)


# Formatierte Monatslabels erzeugen
print(dhService.df_merge_zins.columns)
dhService.df_merge_zins.rename(columns={'jahr': 'year', 'monat': 'month'}, inplace=True)
dhService.df_merge_zins['zeit'] = pd.to_datetime(dhService.df_merge_zins[['year', 'month']].assign(day=1))
df_merge_zins = dhService.df_merge_zins.sort_values('zeit')  # Sortieren nach Zeit

labels = df_merge_zins['zeit'].dt.strftime('%Y-%m')

# Plot erstellen
fig, ax1 = plt.subplots(figsize=(16, 6))

# Kaufpreis (linke y-Achse)
ax1.plot(df_merge_zins['zeit'], df_merge_zins['median_kaufpreis'],
         color='blue', marker='o', label='Median Kaufpreis')
ax1.set_ylabel('Kaufpreis [CHF]', color='blue')
ax1.tick_params(axis='y', labelcolor='blue')

# Hypozins (rechte y-Achse)
ax2 = ax1.twinx()
ax2.plot(df_merge_zins['zeit'], df_merge_zins['festhypo_median'],
         color='red', marker='s', linestyle='--', label='Festhypothekarzins')
ax2.set_ylabel('Hypothekarzins [%]', color='red')
ax2.tick_params(axis='y', labelcolor='red')

# Monatliche Labels setzen
ax1.set_xticks(df_merge_zins['zeit'])
ax1.set_xticklabels(labels, rotation=45, fontsize=8)

# Gitternetzlinien aktivieren
ax1.grid(True)

# Titel und Layout
plt.title('Vergleich: Median-Kaufpreis und Hypothekarzins pro Monat')
ax1.set_xlabel('Monat')

# Legende für beide Achsen anzeigen
fig.legend(loc='upper left', bbox_to_anchor=(0.11, 0.9))

plt.tight_layout()
plt.show()