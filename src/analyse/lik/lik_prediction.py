import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import dataService as ds
import numpy as np
import matplotlib.pyplot as matplot

## PREDICTION - polynomial regression
coeffs = np.polyfit(ds.dfLikBig['jahr'], ds.dfLikBig['lik'], deg=2)
poly_model = np.poly1d(coeffs)

# Predict
future_years = np.arange(2024, 2034)
predicted_lip = poly_model(future_years)

# Plot
matplot.figure(figsize=(10, 5))
matplot.plot(ds.dfLikBig['jahr'], ds.dfLikBig['lik'], label='LIK (historisch)', marker='o', color='royalblue')
matplot.plot(future_years, predicted_lip, label='LIP (Vorhersage)', marker='x', linestyle='--', color='orange')
matplot.plot(np.concatenate((ds.dfLikBig['jahr'], future_years)), poly_model(np.concatenate((ds.dfLikBig['jahr'], future_years))), 
         label='Polynomialer Trend', linestyle=':', color='green')

matplot.title('LIP Vorhersage mit Polynomialer Regression')
matplot.xlabel('Jahr')
matplot.ylabel('Infaltionsrate')
matplot.legend()
matplot.grid(True)
matplot.show()