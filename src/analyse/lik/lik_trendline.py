import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from dataService import dfLik
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

## TRENDLINE
slope, intercept, r_value, p_value, std_err = stats.linregress(dfLik['Jahr'], dfLik['lik'])
lik_trend = slope * dfLik['Jahr'] + intercept

def moving_average(data, window_size):
    return np.convolve(data, np.ones(window_size)/window_size, mode='valid')

lik_moving_avg = moving_average(dfLik['lik'], window_size=3)

plt.figure(figsize=(10, 5))
plt.plot(dfLik['Jahr'], dfLik['lik'], label='LIK', marker='o', color='royalblue')

## ohne moving average
##plt.plot(df['Jahr'], lik_trend, label='LIK Trend', marker='s', color='orange') 

plt.plot(dfLik['Jahr'][1:-1], lik_moving_avg, label='LIK Moving Average', marker='s', color='orange', linestyle='--')

plt.title('LIK Trend')
plt.xlabel('Jahr')
plt.ylabel('Inflationsrate')
plt.legend()
plt.grid(True)
plt.show()
