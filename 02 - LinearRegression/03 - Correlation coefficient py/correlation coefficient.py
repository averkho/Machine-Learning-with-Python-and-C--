# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 15:14:33 2022

@author: Alexander
"""

import numpy as np
from scipy import stats
import pandas as pd

dat=pd.read_csv('../00 -  Data/turbine.csv')

X_variables=['Gas flow', 'Air flow','Temp']
y_variable='MW out'

def pearson_scipy():
    
    '''
    Calculation for peatrson correlation coefficients using scipy library
    '''

    for x in X_variables:
        
        print('Pearson coefficient for {} and {} is {}'.format(x,y_variable,
            np.round(stats.pearsonr(dat[x],dat[y_variable])[0],3)))
    
def pearson_calculation(x_variable,y_variable):
    
    '''
    Calculation pearson correlation coefficient from scratch
    
    '''
    
    x_mean=dat[x_variable].mean()
    y_mean=dat[y_variable].mean()
    
    sum_nomin=0
    sum_denom_x=0
    sum_denom_y=0
    
    for i in range(dat.shape[0]):
        
        sum_nomin+=(dat.iloc[i][x_variable]-x_mean)*(dat.iloc[i][y_variable]-y_mean)
        sum_denom_x+=((dat.iloc[i][x_variable]-x_mean)**2)
        sum_denom_y+=((dat.iloc[i][y_variable]-y_mean)**2)
        
    return np.round(sum_nomin/(np.sqrt(sum_denom_x*sum_denom_y)),3)
        
    
    
if __name__=="__main__":
    
    pearson_scipy()
    print('Calculation of pearson coefficient from scratch ')
    for x in X_variables:
        print('Pearson correlation coef for {} and {} is {}'.
              format(x,y_variable,pearson_calculation(x,y_variable)))
    