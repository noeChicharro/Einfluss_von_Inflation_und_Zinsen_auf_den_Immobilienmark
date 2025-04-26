import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from dataService import dfWohn
import matplotlib.pyplot as plt
import squarify
import plotly.express as px

colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']

df_long = dfWohn.melt(
    id_vars=['jahr'], 
    value_vars=['gemeindetyp_1', 'gemeindetyp_2', 'gemeindetyp_3', 'gemeindetyp_4', 'gemeindetyp_5'],
    var_name='gemeinde',
    value_name='value'
)

print(df_long)

dfGemeindetypen = df_long.groupby('gemeinde')['value'].sum().reset_index()
dfGemeindetypen = dfGemeindetypen.sort_values(by='value', ascending=False)

print(dfGemeindetypen)


plt.figure(figsize=(10, 6))
squarify.plot(
    sizes=dfGemeindetypen['value'], 
    label=dfGemeindetypen['gemeinde'], 
    color=colors, 
    alpha=0.8
)
plt.axis('off')
plt.title("Wohneigentum in Gemeindetypen")
plt.show()