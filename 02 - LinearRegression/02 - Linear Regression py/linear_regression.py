# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 09:23:46 2022

@author: AVERKHO
"""
import numpy as np
import matplotlib.pyplot as plt
plt.close('all')
import pandas as pd

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error as mse

from utils import Utils

dat=pd.read_csv('../00 -  Data/turbine.csv')

    

def regression_sklearn():
    
    #dat['Temp_sqrt']=dat['Temp']**2
    X=dat['Temp']
    y=dat['MW out']
    
    lr=LinearRegression()
    lr.fit(X.values.reshape(-1,1),y.values.reshape(-1,1))
    pred=lr.predict(X.values.reshape(-1,1))
    
    np.linalg.lstsq(X.values.reshape(-1,1),y.values.reshape(-1,1))
    
    print('Rank of matrix is {}'.format(np.round(lr.rank_)))
    print('Coefficient is {}'.format(np.round(lr.coef_[0][0],2)))
    print('Intercept is {}'.format(np.round(lr.intercept_[0],2)))
    
    print('MW output = {} + ({}) x Temperature'.format(np.round(lr.intercept_[0],2),np.round(lr.coef_[0][0],2)))
    
    #kwargs={'color':Utils.purple_hex,'fontweight':'bold','fontproperties':{'family':Utils.csfont,'size':20}}
    
    fig=plt.figure(1)
    ax=fig.add_subplot(111)
    ax.scatter(dat['Temp'],y,color=Utils.green_hex)
    ax.plot(dat['Temp'],pred,color=Utils.red_hex,marker='_',lw=4)
    
    ax.set_xlabel('Temperature',**Utils.ax_kwargs)
    ax.set_ylabel('MW',**Utils.ax_kwargs)
    
    fig.patch.set_facecolor(Utils.black_hex)
    ax.set_facecolor(Utils.black_hex)
    for spine in ax.spines.values():
        spine.set_edgecolor(Utils.white_hex)
        spine.set(linewidth=3)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.set_title('Regression mse={}'.format(np.round(mse(y,pred),2)),**Utils.ax_kwargs)
    ax.tick_params(axis='x', colors=Utils.purple_hex,labelsize=15)
    ax.tick_params(axis='y', colors=Utils.purple_hex,labelsize=15)
    ax.grid(True,**Utils.grid_kwargs)
    plt.tight_layout()
    
def regresion_closed_form_solution(dat):
    
    '''
    Closed form solution for regression. 
    
    theta=(X^T*X)^(-1)*X^T*y
    
    X - feature matrix (n*(d+1))
    y - vector (n*1)
    d - number of features
    n - number of samples
    
    return 

    y_pred - vector of predicted values (n*1)
    theta - vector of parameters ((d+1)*1)
    
    '''
    
    X=dat['Temp'].values.reshape(-1,1)
    y=dat['MW out'].values.reshape(-1,1)
    A=np.ones((len(X),1))
    X=np.hstack((A,X))
    
    theta=np.matmul(np.linalg.inv(np.matmul(np.transpose(X),X)),np.matmul(np.transpose(X),y))
    y_pred=np.matmul(X,theta)
    
    return y_pred,theta


if __name__=="__main__":
    
    dat=pd.read_csv('../00 -  Data/turbine.csv')
    regression_sklearn()
    
     
    y_pred,theta=regresion_closed_form_solution(dat)
    
    

