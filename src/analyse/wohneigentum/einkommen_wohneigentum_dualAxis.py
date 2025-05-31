import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import matplotlib.pyplot as plt
from dataService import dfCommonWohnEinkommen

fig, ax1 = plt.subplots(figsize=(12, 6))

# Wohneigentum on left axis
ax1.bar(dfCommonWohnEinkommen['jahr'], dfCommonWohnEinkommen['total'], width=0.4, align='edge', color='steelblue', label='Wohneigentum')
ax1.set_ylabel('Wohneigentum (CHF)', color='steelblue')
ax1.tick_params(axis='y', labelcolor='steelblue')

# Einkommen on right axis
ax2 = ax1.twinx()
ax2.bar(dfCommonWohnEinkommen['jahr'], dfCommonWohnEinkommen['Einkommen_unselbstaendige_Erwerbstaetigkeit'], width=-0.4, align='edge', color='salmon', label='Einkommen')
ax2.set_ylabel('Einkommen (CHF)', color='salmon')
ax2.tick_params(axis='y', labelcolor='salmon')

plt.title('Wohneigentum vs. Einkommen (Dual-Axis)')
plt.xticks(dfCommonWohnEinkommen['jahr'])
plt.grid(True, axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()