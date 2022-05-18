# -*- coding: utf-8 -*-
"""
Created on Wed May 18 09:14:52 2022

@author: AVERKHO
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.close('all')

from sklearn.decomposition import PCA 
from sklearn.preprocessing import StandardScaler
from utils import Utils

dat=pd.read_excel('./Credit score.xlsx')

pca=PCA(n_components=8)

scaler=StandardScaler()
X=scaler.fit_transform(dat)

scores=pca.fit_transform(X)

#eigendecomposition

X_cov=np.cov(X.T)

W,V=np.linalg.eig(X_cov)

D=np.diag(W)

'''
eigenvalues decomposition

C = V x W x V.T

'''

C=np.matmul(np.matmul(V,D),V.T)

'''

Score plot calculation X * V

'''
T=np.matmul(X,V)

fig=plt.figure(1,figsize=(10,8))
ax=fig.add_subplot(111)
ax.scatter(T[:,0],T[:,1],s=100,color=Utils.red_hex)
ax.axhline(0,color=Utils.white_hex)
ax.axvline(0,color=Utils.white_hex)
fig.patch.set_facecolor(Utils.black_hex)


ax.set_facecolor(Utils.black_hex)
for spine in ax.spines.values():
    spine.set_edgecolor(Utils.white_hex)
spine.set(linewidth=3)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.set_title('Score plot of PC1 vs. PC2',color=Utils.purple_hex,
                 fontproperties={'family':Utils.csfont,'size':20})
ax.tick_params(axis='x', colors=Utils.purple_hex,labelsize=15)
ax.tick_params(axis='y', colors=Utils.purple_hex,labelsize=15)

ax.set_xlabel('PC1',color=Utils.purple_hex,fontweight='bold',
                      fontproperties={'family':Utils.csfont,'size':20})
ax.set_ylabel('PC2',color=Utils.purple_hex,fontweight='bold',
                      fontproperties={'family':Utils.csfont,'size':20})

ax.grid(Utils.grid_kwargs)
for i in range(T.shape[0]):
    
    ax.text(T[i][0],T[i][1]+0.1,str(i),color=Utils.purple_hex)    
    
plt.tight_layout()

'''

Loading plot

'''

fig=plt.figure(2,figsize=(10,8))
ax=fig.add_subplot(111)
ax.scatter(V[:,0],V[:,1],s=100,color=Utils.red_hex)
ax.axhline(0,color=Utils.white_hex)
ax.axvline(0,color=Utils.white_hex)
fig.patch.set_facecolor(Utils.black_hex)


ax.set_facecolor(Utils.black_hex)
for spine in ax.spines.values():
    spine.set_edgecolor(Utils.white_hex)
spine.set(linewidth=3)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.set_title('Loading plot of PC1 vs. PC2',color=Utils.purple_hex,
                 fontproperties={'family':Utils.csfont,'size':20})
ax.tick_params(axis='x', colors=Utils.purple_hex,labelsize=15)
ax.tick_params(axis='y', colors=Utils.purple_hex,labelsize=15)

ax.set_xlabel('PC1',color=Utils.purple_hex,fontweight='bold',
                      fontproperties={'family':Utils.csfont,'size':20})
ax.set_ylabel('PC2',color=Utils.purple_hex,fontweight='bold',
                      fontproperties={'family':Utils.csfont,'size':20})

ax.grid(Utils.grid_kwargs)
for i in range(T.shape[1]):
    
    ax.text(V[i][0],V[i][1]+0.01,dat.columns[i],color=Utils.purple_hex,size=14)    
    
plt.tight_layout()

'''
Dcree plot

'''

fig=plt.figure(3,figsize=(10,8))
ax=fig.add_subplot(111)
box=ax.bar(np.arange(len(W)),W)
ax.axhline(0,color=Utils.white_hex)
ax.axvline(0,color=Utils.white_hex)
fig.patch.set_facecolor(Utils.black_hex)


ax.set_facecolor(Utils.black_hex)
for spine in ax.spines.values():
    spine.set_edgecolor(Utils.white_hex)
spine.set(linewidth=3)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.set_title('Scree plot',color=Utils.purple_hex,
                 fontproperties={'family':Utils.csfont,'size':20})
ax.tick_params(axis='x', colors=Utils.purple_hex,labelsize=15)
ax.tick_params(axis='y', colors=Utils.purple_hex,labelsize=15)

ax.set_xlabel('Component number',color=Utils.purple_hex,fontweight='bold',
                      fontproperties={'family':Utils.csfont,'size':20})
ax.set_ylabel('Eigenvalue',color=Utils.purple_hex,fontweight='bold',
                      fontproperties={'family':Utils.csfont,'size':20})

ax.grid(Utils.grid_kwargs)

    
plt.tight_layout()


