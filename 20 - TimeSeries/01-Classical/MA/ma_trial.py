#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 14:51:28 2022

@author: alexander
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.close('all')
from statsmodels.tsa.stattools import acf,pacf

errors = np.random.normal(0,1,4000)
date_index = pd.date_range(start = '01.01.2020', end = '01.06.2022')

np.random.seed(10)
mu = 50
series = []
for t in range(len(date_index)):
    
    if t == 0:
        series.append(mu + errors[t])
    elif t == 1:
        series.append(mu + 0.4 * errors[t-1] + errors[t])
    else:
        series.append(mu + 0.4 * errors[t-1] + 0.3 * errors[t-2] + errors[t])
    
dat = pd.DataFrame(series,index = date_index, columns = ['value'])

fig = plt.figure(1)
ax = fig.add_subplot(111)
ax.plot(dat['value'], color = '#00FF00')
fig.patch.set_facecolor((0,0,0,1))
ax.set_facecolor('#000000')
for spine in ax.spines.values():
    spine.set_edgecolor('#FFFFFF')
    spine.set(linewidth=3)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.set_title(r'MA model $y_t = 50 + 0.4\epsilon_{t-1} + 0.3\epsilon_{t-2} + \epsilon_t$ ', 
          {'color':'#00FFFF','fontweight':'bold','fontproperties':{'family':'Comic Sans MS','size':20}})

ax.tick_params(axis='x', colors='#00FFFF',labelsize=15)
ax.tick_params(axis='y', colors='#00FFFF',labelsize=15)
ax.grid(True,color = '#FFFFFF', linestyle = '--')

#plt.title(r'MA model {mu} + 04 * $\alpha_i', color = '#00FFFF') 

acf_values = acf(series)

acf_dat = pd.DataFrame(series,columns=['0_lag'])
for lag in range(1,11):
    
    acf_dat[str(lag)+'_lag'] = acf_dat['0_lag'].shift(lag)
    

def calculate_acf(lags = 20):
    acf_ = []
    df = pd.DataFrame(acf_dat['0_lag'])
    for i in range(0,lags):
            
        df[f'{i}_lag'] = df['0_lag'].shift(i)
        df = df[df[f'{i}_lag'].notna()]
        acf_.append(np.corrcoef(df['0_lag'],df[f'{i}_lag'])[0,1])

    return acf_


fig = plt.figure(2)
ax = fig.add_subplot(111)
ax.bar(np.arange(len(acf_values)),acf_values,color = '#00FF00')
fig.patch.set_facecolor((0,0,0,1))
ax.set_facecolor('#000000')
for spine in ax.spines.values():
    spine.set_edgecolor('#FFFFFF')
    spine.set(linewidth=3)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.set_title('Auto correlation function ACF', 
             {'color':'#00FFFF','fontweight':'bold','fontproperties':{'family':'Comic Sans MS','size':20}})
ax.tick_params(axis='x', colors='#00FFFF',labelsize=15)
ax.tick_params(axis='y', colors='#00FFFF',labelsize=15)
ax.grid(True,color = '#FFFFFF', linestyle = '--')



