from sqlalchemy import create_engine
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import matplotlib.pyplot as matplot

engine = create_engine('mysql+mysqlconnector://root:Wuschtel5!@localhost/bina', echo=False)
cursor = engine.raw_connection().cursor()

selectQuery = """
    SELECT Jahr, lik, hvpi
    FROM inflationsrate
"""
cursor.execute(selectQuery)
cursor.close()

df = pd.read_sql(selectQuery, engine)
print(df.head())
engine.dispose()

x = np.arange(len(df['Jahr']))
width = 0.35

plt.figure(figsize=(10, 5))
plt.bar(x - width/2, df['lik'], width, label='LIK', color='royalblue')
plt.bar(x + width/2, df['hvpi'], width, label='HVPI', color='crimson')

plt.xticks(x, df['Jahr'])
plt.xlabel('Jahr')
plt.ylabel('Inflationsrate')
plt.title('LIK vs HVPI')
plt.legend()
plt.grid(axis='y')
plt.show()

## TRENDLINE
slope, intercept, r_value, p_value, std_err = stats.linregress(df['Jahr'], df['lik'])
lik_trend = slope * df['Jahr'] + intercept

def moving_average(data, window_size):
    return np.convolve(data, np.ones(window_size)/window_size, mode='valid')

lik_moving_avg = moving_average(df['lik'], window_size=3)

plt.figure(figsize=(10, 5))
plt.plot(df['Jahr'], df['lik'], label='LIK', marker='o', color='royalblue')

## ohne moving average
##plt.plot(df['Jahr'], lik_trend, label='LIK Trend', marker='s', color='orange') 

plt.plot(df['Jahr'][1:-1], lik_moving_avg, label='LIK Moving Average', marker='s', color='orange', linestyle='--')

plt.title('LIK Trend')
plt.xlabel('Jahr')
plt.ylabel('Inflationsrate')
plt.legend()
plt.grid(True)
plt.show()


## PREDICTION - linear regression
slop, intercept, _, _, _= stats.linregress(df['Jahr'], df['lik'])
future_years = np.arange(2024, 2034)
prodiction = slop * future_years + intercept

combi_years = np.concatenate((df['Jahr'], future_years))
combi_lik = np.concatenate((df['lik'], prodiction))

matplot.figure(figsize=(10, 5))
matplot.plot(df['Jahr'], df['lik'], label='LIK', marker='o', color='royalblue')
matplot.plot(future_years, prodiction, label='LIK Vorhersage', marker='s', color='orange')
matplot.plot(combi_years, slope * combi_years + intercept, label='LIK Trend', linestyle=':', color='green')

matplot.title('LIK Vorhersage')
matplot.xlabel('Jahr')
matplot.ylabel('Inflationsrate')
plt.legend()
plt.grid(True)
plt.show()

## PREDICTION - polynomial regression
coeffs = np.polyfit(df['Jahr'], df['lik'], deg=2)
poly_model = np.poly1d(coeffs)

# Predict
future_years = np.arange(2024, 2034)
predicted_lip = poly_model(future_years)

# Plot
matplot.figure(figsize=(10, 5))
matplot.plot(df['Jahr'], df['lik'], label='LIK (historisch)', marker='o', color='royalblue')
matplot.plot(future_years, predicted_lip, label='LIP (Vorhersage)', marker='x', linestyle='--', color='orange')
matplot.plot(np.concatenate((df['Jahr'], future_years)), poly_model(np.concatenate((df['Jahr'], future_years))), 
         label='Polynomialer Trend', linestyle=':', color='green')

matplot.title('LIP Vorhersage mit Polynomialer Regression')
matplot.xlabel('Jahr')
matplot.ylabel('Infaltionsrate')
matplot.legend()
matplot.grid(True)
matplot.show()