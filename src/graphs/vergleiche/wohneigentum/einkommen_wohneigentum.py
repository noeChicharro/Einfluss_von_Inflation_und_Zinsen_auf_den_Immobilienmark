import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import matplotlib.pyplot as plt
import numpy as np
from dataService import dfCommonWohnEinkommen

x = np.arange(len(dfCommonWohnEinkommen['jahr']))  
width = 0.35  

plt.figure(figsize=(12, 6))

plt.bar(x - width/2, dfCommonWohnEinkommen['total'], width, label='Wohneigentum', color='steelblue')
plt.bar(x + width/2, dfCommonWohnEinkommen['Einkommen_unselbstaendige_Erwerbstaetigkeit'], width, label='Einkommen', color='salmon')

plt.xticks(x, dfCommonWohnEinkommen['jahr'])
plt.xlabel('Jahr')
plt.ylabel('Wert')
plt.title('Vergleich von Wohneigentum und Einkommen ab 2017')
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()




