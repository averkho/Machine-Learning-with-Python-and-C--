# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 16:13:11 2022

@author: AVERKHO
"""

# https://github.com/eriklindernoren/ML-From-Scratch/blob/master/mlfromscratch/supervised_learning/regression.py

import numpy as np
import pandas as pd

from sklearn.linear_model import LinearRegression, Ridge

from sklearn.metrics import mean_squared_error as mse
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler, PolynomialFeatures

plt.close('all')

class Regression(object):
    
    def __init__(self,n_iterations,learning_rate,fit_intercept=True):
        
        self.n_iterations=n_iterations
        self.learning_rate=learning_rate
        self.fit_intercept=fit_intercept
        
    def initialize_weights(self,n_features):
        
        limit=1/np.sqrt(n_features)
        self.w=np.random.uniform(-limit,limit,(n_features))
        
    def fit(self,X,y):
        
        if self.fit_intercept:
            X=np.insert(X,0,1,axis=1)

def linear_regression(X,y,scaling=True,polynomial=True):
    
    lr=LinearRegression()
    
    scaler=StandardScaler()
    
    X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.33)
    
    if scaling:
        
        scaler.fit(X_train)
        X_train=scaler.transform(X_train)
        X_test=scaler.transform(X_test)
        
    if polynomial:
        
        polynomial=PolynomialFeatures(degree=3,interaction_only=True)
        X_train=polynomial.fit_transform(X_train)
        X_test=polynomial.fit_transform(X_test)
        
        
    
    lr.fit(X_train,y_train)
    
    pred_train=lr.predict(X_train)
    pred_test=lr.predict(X_test)
    
    final_dat_train=pd.DataFrame({'fact':y_train,'predicted':pred_train})
    
    final_dat_test=pd.DataFrame({'fact':y_test,'predicted':pred_test})
    
    final_dat=pd.concat([final_dat_train,final_dat_test],axis=0)
    
    final_dat.reset_index(inplace=True,drop=True)
    
    fig=plt.figure(1)
    ax=fig.add_subplot(111)
    ax.plot(final_dat['fact'],color='red')
    ax.plot(final_dat['predicted'],color='black')
    ax.axvline(int(dat.shape[0]*(1-0.33)))
    
    print('TRAIN error')
    print('Root mean squared erro is {}'.format(np.sqrt(mse(pred_train,y_train))))
    print('Root mean squared erro is {} %'.format(np.sqrt(mse(pred_train,y_train))/np.mean(y_train)*100))
    
    print('TEST error')
    print('Root mean squared erro is {}'.format(np.sqrt(mse(pred_test,y_test))))
    print('Root mean squared erro is {} %'.format(np.sqrt(mse(pred_test,y_test))/np.mean(y_test)*100))
    
def ridge_regression(X,y,alpha,scaling=True,polynomial=True):
    
    lr=Ridge(alpha=alpha)
    
    X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.33)
    
    scaler=StandardScaler()
    
    if scaling:
        
        X_train=scaler.fit_transform(X_train)
        X_test=scaler.transform(X_test)
    
    if polynomial:
        
        polynomial=PolynomialFeatures(degree=3,interaction_only=True)
        X_train=polynomial.fit_transform(X_train)
        X_test=polynomial.fit_transform(X_test)
    
    lr.fit(X_train,y_train)
    
    pred_train=lr.predict(X_train)
    pred_test=lr.predict(X_test)
    
    final_dat_train=pd.DataFrame({'fact':y_train,'predicted':pred_train})
    
    final_dat_test=pd.DataFrame({'fact':y_test,'predicted':pred_test})
    
    final_dat=pd.concat([final_dat_train,final_dat_test],axis=0)
    
    final_dat.reset_index(inplace=True,drop=True)
    
    fig=plt.figure(1)
    ax=fig.add_subplot(111)
    ax.plot(final_dat['fact'],color='red')
    ax.plot(final_dat['predicted'],color='black')
    ax.axvline(int(dat.shape[0]*(1-0.33)))
    
    print('TRAIN error')
    print('Root mean squared erro is {}'.format(np.sqrt(mse(pred_train,y_train))))
    print('Root mean squared erro is {} %'.format(np.sqrt(mse(pred_train,y_train))/np.mean(y_train)*100))
    
    print('TEST error')
    print('Root mean squared erro is {}'.format(np.sqrt(mse(pred_test,y_test))))
    print('Root mean squared erro is {} %'.format(np.sqrt(mse(pred_test,y_test))/np.mean(y_test)*100))

if __name__=="__main__":
    
    
    
    dat=pd.read_csv('./archive/ParisHousing.csv')
    
    y=dat['price']
    X=dat[['squareMeters', 'numberOfRooms', 'hasYard', 'hasPool', 'floors',
       'cityCode', 'cityPartRange', 'numPrevOwners', 'made', 'isNewBuilt',
       'hasStormProtector', 'basement', 'attic', 'garage', 'hasStorageRoom',
       'hasGuestRoom']]
    
    
    dat=pd.read_csv('./archive/boston.csv')
    
    y=dat['MEDV']
    X=dat[['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX',
       'PTRATIO', 'B', 'LSTAT']]
    
    
    
    linear_regression(X,y,scaling=True)
    
    ridge_regression(X,y,alpha=0.1,scaling=True)
    
    
    
    
    