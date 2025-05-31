import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from dataService import dfDataHive
import seaborn as sns
import matplotlib.pyplot as plt

# Optional: filter out rows with missing values in either column
df_clean = dfDataHive[['price_per_sqr_meter', 'canton']].dropna()

sorted_cantons = (
    df_clean.groupby('canton')['price_per_sqr_meter']
    .median()
    .sort_values()
    .index
)

# Set up the plot
plt.figure(figsize=(14, 6))
sns.boxplot(data=df_clean, x='canton', y='price_per_sqr_meter', order=sorted_cantons)

# Make it readable
plt.xticks(rotation=45)
plt.title('Price per Square Meter by Canton')
plt.xlabel('Canton')
plt.ylabel('Price per Square Meter (CHF)')
plt.ylim(100, df_clean['price_per_sqr_meter'].max() * 1.05)
plt.grid(True, axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()


