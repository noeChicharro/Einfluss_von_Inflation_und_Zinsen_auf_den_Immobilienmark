import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from dataService import dfDataHive
import pandas as pd
import matplotlib.pyplot as plt
import squarify  # Make sure to install it: pip install squarify

# Prepare data: drop NaNs
df_treemap = dfDataHive[['canton', 'price_per_sqr_meter']].dropna()

# Aggregate: mean price and count per canton
agg_data = df_treemap.groupby('canton').agg(
    avg_price=('price_per_sqr_meter', 'mean'),
    count=('price_per_sqr_meter', 'count')
).reset_index()

# Size by number of listings, color by average price
sizes = agg_data['count']
labels = [f"{c}\n{p:,.0f} CHF/m²" for c, p in zip(agg_data['canton'], agg_data['avg_price'])]
colors = agg_data['avg_price']  # Higher price = deeper color

# Create treemap
plt.figure(figsize=(14, 8))
squarify.plot(sizes=sizes, label=labels, color=plt.cm.viridis(colors / max(colors)), alpha=0.9)
plt.axis('off')
plt.title('Average Price per Square Meter by Canton (Treemap)', fontsize=16)
plt.show()