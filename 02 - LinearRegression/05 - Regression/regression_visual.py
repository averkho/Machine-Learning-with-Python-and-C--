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
from sklearn.metrics import mean_squared_error

from utils import Utils

np.random.seed(102)

X=np.arange(0.01,10,0.1)
y=np.zeros(len(X))

for i,x in enumerate(X):
    
    y[i]=(x**2+np.random.normal(0,10,1))
    
    
dat=pd.DataFrame({'x':X,'y':y})

dat['x2']=dat['x']**2
dat['x3']=dat['x']**3
dat['x4']=dat['x']**4
dat['x6']=dat['x']**6
dat['x8']=dat['x']**8

lr=LinearRegression()

cols=['x','x2','x3','x4','x6']

X=dat[['x','x2','x3','x4','x6','x8']]
y=dat['y']

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.33,shuffle=True)

lr.fit(X_train.values,y_train.values.reshape(-1,1))

pred_train=lr.predict(X_train.values)
pred_test=lr.predict(X_test.values)

#mse[]

pred_train=pd.DataFrame(pred_train,columns=['predicted'])
pred_train['x']=X_train['x'].values

pred_train=pred_train.sort_values(by='x',ascending=True)
pred_train.reset_index(inplace=True,drop=True)

    
fig=plt.figure(1)
ax=fig.add_subplot(111)
ax.scatter(X_train['x'],y_train,color=Utils.blue_hex)
ax.plot(pred_train['x'].values,pred_train['predicted'],color=Utils.red_hex,lw=4)
fig.patch.set_facecolor(Utils.black_hex)
ax.set_facecolor(Utils.black_hex)
for spine in ax.spines.values():
    spine.set_edgecolor(Utils.white_hex)
    spine.set(linewidth=3)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.tick_params(axis='x', colors=Utils.purple_hex,labelsize=15)
ax.tick_params(axis='y', colors=Utils.purple_hex,labelsize=15)
ax.grid(True,**Utils.grid_kwargs)
plt.tight_layout()
#ax.scatter(X_test['x'],pred_test,color=Utils.green_hex,marker='o',lw=4)



