# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 10:51:02 2022

@author: AVERKHO
"""
import numpy as np
import matplotlib.pyplot as plt
plt.close('all')
import pandas as pd

from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

from utils import Utils

np.random.seed(528)

MAX_COMPLEXITY=10

def create_data():
    
    '''
    Creating data for further demostration
    
    '''
    X=np.arange(0.01,10,0.1)
    y=np.zeros(len(X))
    
    for i,x in enumerate(X):
        
        y[i]=(x**2+np.random.normal(0,10,1))
        
    dat=pd.DataFrame({'x':X,'y':y})
    
    # Ading complexity to the model
    col=['x']
    cols=['x'+str(col) for col in range(1,MAX_COMPLEXITY+1)]
    cols=col+cols
    #cols=['x','x2','x3','x4','x6','x8']
    for col in cols[1:]:
        
        dat[col]=dat['x']**int(str(col)[-1])
    
    y=dat['y']
    X=dat[cols]
    
    
    return X,y

def fit_regression_model(X,y,complexity,l2=None):
    
    if l2!=None:
        
        lr=Lasso(alpha=l2)
    else:
        lr=LinearRegression()
    
    X=X[X.columns[:complexity]]
      
    X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.33,shuffle=True)
    
    lr.fit(X_train.values,y_train.values.reshape(-1,1))
    
    pred_train=lr.predict(X_train.values)
    pred_test=lr.predict(X_test.values)
    
    #mse[]
    
    mse_train=np.round(mean_squared_error(y_train,pred_train),1)
    mse_test=np.round(mean_squared_error(y_test,pred_test),2)
    
    pred_train=pd.DataFrame(pred_train,columns=['predicted'])
    pred_train['x']=X_train['x'].values
    
    pred_train=pred_train.sort_values(by='x',ascending=True)
    pred_train.reset_index(inplace=True,drop=True)
    
    
       
    
    equation='Y='
    
    for j in range(1,complexity+1):
        
        if j!=complexity:
            
            equation+='b{} x X^{} + '.format(j,j)
        
        else:
            
            equation+='b{} x X^{}'.format(j,j)
        
    print(equation)    
    fig=plt.figure(complexity,figsize=(12,8))
    ax=fig.add_subplot(111)
    ax.scatter(X_train['x'],y_train,color=Utils.blue_hex)
    ax.scatter(X_test['x'],y_test,color=Utils.green_hex)
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
    ax.set_title('Training MSE={} Testing MSE={}'.format(mse_train,mse_test),color=Utils.purple_hex,
                     fontproperties={'family':Utils.csfont,'size':20})
    ax.set_xlabel('X',fontproperties={'family':Utils.csfont,'size':14},color=Utils.purple_hex)
    ax.set_ylabel('Y',fontproperties={'family':Utils.csfont,'size':14},color=Utils.purple_hex)
    ax.text(0,102,equation,fontproperties={'family':Utils.csfont,'size':14},color=Utils.purple_hex)
    plt.tight_layout()
    
    
    
    return mse_train,mse_test
#ax.scatter(X_test['x'],pred_test,color=Utils.green_hex,marker='o',lw=4)

def plot_lines(MSE_train_test):
    
    fig=plt.figure(MAX_COMPLEXITY,figsize=(12,8))
    ax=fig.add_subplot(111)
    ax.plot(MSE_train_test['mse_train'],color=Utils.red_hex,lw=4,label='training error',marker='o')
    ax.plot(MSE_train_test['mse_test'],color=Utils.blue_hex,lw=4,label='testing error',marker='o')
    
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
    ax.set_xlabel('model complexity',fontproperties={'family':Utils.csfont,'size':14},color=Utils.purple_hex)
    ax.set_ylabel('error',fontproperties={'family':Utils.csfont,'size':14},color=Utils.purple_hex)
    ax.set_title('Error and model complexity'.format(mse_train,mse_test),color=Utils.purple_hex,
                     fontproperties={'family':Utils.csfont,'size':20})
    ax.legend()

if __name__=="__main__":
    
    MSE_train,MSE_test=[],[]
    X,y=create_data()
    for j in range(1,MAX_COMPLEXITY):
        
        mse_train,mse_test=fit_regression_model(X,y,complexity=j)
        MSE_train.append(mse_train)
        MSE_test.append(mse_test)

    MSE_train_test=pd.DataFrame({'mse_train':MSE_train,'mse_test':MSE_test})
    plot_lines(MSE_train_test)
    
    
    
    