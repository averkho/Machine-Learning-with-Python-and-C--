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

from utils import Utils

dat=pd.read_csv('../00 -  Data/turbine.csv')

def regression_sklearn():

    X=dat['Temp']
    y=dat['MW out']
    
    lr=LinearRegression()
    lr.fit(X.values.reshape(-1,1),y.values.reshape(-1,1))
    pred=lr.predict(X.values.reshape(-1,1))
    
    
    #kwargs={'color':Utils.purple_hex,'fontweight':'bold','fontproperties':{'family':Utils.csfont,'size':20}}
    
    fig=plt.figure(1)
    ax=fig.add_subplot(111)
    ax.scatter(X,y,color=Utils.green_hex)
    ax.plot(X,pred,color=Utils.red_hex,marker='_',lw=4)
    
    ax.set_xlabel('Temperature',**Utils.ax_kwargs)
    ax.set_ylabel('MW',**Utils.ax_kwargs)
    
    fig.patch.set_facecolor(Utils.black_hex)
    ax.set_facecolor(Utils.black_hex)
    for spine in ax.spines.values():
        spine.set_edgecolor(Utils.white_hex)
        spine.set(linewidth=3)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.set_title('Regression',**Utils.ax_kwargs)
    ax.tick_params(axis='x', colors=Utils.purple_hex,labelsize=15)
    ax.tick_params(axis='y', colors=Utils.purple_hex,labelsize=15)
    ax.grid(True,**Utils.grid_kwargs)
    plt.tight_layout()
    

    
X=np.array(dat['Temp'])
y=np.array(dat['MW out'])
    

'''
if __name__=="__main__":
    
    dat=pd.read_csv('../00 -  Data/turbine.csv')
    regression_sklearn()

'''