#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 15 18:06:02 2022

@author: alexander
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.close('all')
import os
import seaborn as sns
from dask.dataframe import from_pandas
from tqdm import tqdm
import dask

from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

from multiprocessing import Pool

import catboost as cat

path='home/alexander/DataScience/Kaggle/TokyoStock/'

folders=os.listdir('./jpx-tokyo-stock-exchange-prediction')
print(folders)

path='./jpx-tokyo-stock-exchange-prediction/train_files/'

files=os.listdir(path)
print(files)
dat_train=pd.read_csv(path+'stock_prices.csv')
dat_sec=pd.read_csv(path+'secondary_stock_prices.csv')

sec_dat=dat_train[['Date','SecuritiesCode','Target']]
prim_dat=dat_sec[['Date','SecuritiesCode','Target']]

prim_dat_pivot=pd.pivot_table(prim_dat,values='Target',index=['Date'],columns=['SecuritiesCode'])
sec_dat_pivot=pd.pivot_table(sec_dat,values='Target',index=['Date'],columns=['SecuritiesCode'])
sec_dat_pivot=sec_dat_pivot.add_suffix('_sec')
prin_sec_dat_pivot=pd.concat([prim_dat_pivot,sec_dat_pivot],axis=1)

prin_sec_dat_pivot.fillna(0,inplace=True)

scaler=StandardScaler()
X=scaler.fit_transform(prin_sec_dat_pivot)

cov_matrix=np.cov(X)
W,V=np.linalg.eig(cov_matrix)

#Eigenvalues decomposition
D=np.diag(W)

#covarinace matrix
C=np.matmul(np.matmul(V,D),V.T)

T=np.matmul(X.T,V)
pca=PCA()
score=pca.fit_transform(X)

pca.score()



