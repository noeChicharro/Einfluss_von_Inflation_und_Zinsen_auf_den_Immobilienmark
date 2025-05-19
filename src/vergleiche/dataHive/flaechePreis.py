import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from dataService import dfDataHive
import seaborn as sns
import matplotlib.pyplot as plt

# Optional: filter out rows with missing values in either column
df_clean = dfDataHive[['price_per_sqr_meter', 'canton']].dropna()

# Set up the plot
plt.figure(figsize=(14, 6))
sns.boxplot(data=df_clean, x='canton', y='price_per_sqr_meter')

# Make it readable
plt.xticks(rotation=45)
plt.title('Price per Square Meter by Canton')
plt.xlabel('Canton')
plt.ylabel('Price per Square Meter (CHF)')
plt.tight_layout()
plt.show()


