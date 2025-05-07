import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from dataService import dfDataHive
import seaborn as sns
import matplotlib.pyplot as plt
avg_price_per_canton = dfDataHive.groupby('canton')['price_per_sqr_meter'].mean().sort_values()

plt.figure(figsize=(14, 6))
avg_price_per_canton.plot(kind='bar', color='skyblue', edgecolor='black')

plt.xlabel('Canton')
plt.ylabel('Average Price per Square Meter (CHF)')
plt.title('Average Price per Square Meter by Canton')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()