# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 10:51:02 2022

@author: AVERKHO
"""
import numpy as np
import matplotlib.pyplot as plt
plt.close('all')
import pandas as pd

from sklearn.linear_model import LinearRegression, Ridge
from sklearn.model_selection import train_test_split

from utils import Utils


X=np.arange(0.01,10,0.1)
y=np.zeros(len(X))

for i,x in enumerate(X):
    
    y[i]=(x+x**2+x**3++np.log(x**10)+np.random.normal(0,100,1))
    
    
dat=pd.DataFrame({'x':X,'y':y})

dat['x2']=dat['x']**2

lr=LinearRegression()



X=dat[['x','x2']]
y=dat['y']

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.33,shuffle=True)

lr.fit(X_train.values,y_train.values.reshape(-1,1))

pred_train=lr.predict(X_train.values)
pred_test=lr.predict(X_test.values)
    
fig=plt.figure(1)
ax=fig.add_subplot(111)
ax.scatter(X,y)
ax.plot(X_train['x'],pred_train,color=Utils.red_hex,marker='_',lw=4)
ax.plot(X_test['x'],pred_test,color=Utils.green_hex,marker='o',lw=4)

