import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from dataService import dfLik
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import matplotlib.pyplot as matplot

## PREDICTION - linear regression
slop, intercept, _, _, _= stats.linregress(dfLik['Jahr'], dfLik['lik'])
future_years = np.arange(2024, 2034)
prodiction = slop * future_years + intercept

combi_years = np.concatenate((dfLik['Jahr'], future_years))
combi_lik = np.concatenate((dfLik['lik'], prodiction))

matplot.figure(figsize=(10, 5))
matplot.plot(dfLik['Jahr'], dfLik['lik'], label='LIK', marker='o', color='royalblue')
matplot.plot(future_years, prodiction, label='LIK Vorhersage', marker='s', color='orange')
matplot.plot(combi_years, slop * combi_years + intercept, label='LIK Trend', linestyle=':', color='green')

matplot.title('LIK Vorhersage')
matplot.xlabel('Jahr')
matplot.ylabel('Inflationsrate')
plt.legend()
plt.grid(True)
plt.show()