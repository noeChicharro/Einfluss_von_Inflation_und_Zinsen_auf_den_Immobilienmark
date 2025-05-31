import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from dataService import dfLik
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(len(dfLik['Jahr']))
width = 0.35

plt.figure(figsize=(10, 5))
plt.bar(x - width/2, dfLik['lik'], width, label='LIK', color='royalblue')
plt.bar(x + width/2, dfLik['hvpi'], width, label='HVPI', color='crimson')

plt.xticks(x, dfLik['Jahr'])
plt.xlabel('Jahr')
plt.ylabel('Inflationsrate')
plt.title('LIK vs HVPI')
plt.legend()
plt.grid(axis='y')
plt.show()