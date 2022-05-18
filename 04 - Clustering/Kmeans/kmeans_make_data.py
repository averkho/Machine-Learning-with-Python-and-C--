# -*- coding: utf-8 -*-
"""
Created on Wed May 11 12:37:07 2022

@author: AVERKHO
"""
import numpy as np
import matplotlib.pyplot as plt
plt.close('all')
from sklearn.datasets import make_blobs
import pandas as pd

from dataclasses import dataclass

@dataclass
class Utils:
    
    
    purple_hex:str='#00FFFF'
    green_hex:str='#00FF00'
    yellow_hex:str='#FFFF00'
    rose_hex:str='#FF00FF'
    red_hex:str='#FF0000'
    blue_hex:str='#0000FF'
    white_hex:str='#FFFFFF'
    black_hex:str='#000000'
    
    purple_rgba:tuple=(0,1,1,1)
    green_rgba:tuple=(0,1,0,1)
    yellow_rgba:tuple=(1,1,0,1)
    rose_rgba:tuple=(1,0,1,1)
    red_rgba:tuple=(1,0,0,1)
    blue_rgba:tuple=(0,0,1,1)
    white_rgba:tuple=(1,1,1,1)
    black_rgba:tuple=(0,0,0,1)
    
    csfont:str='Comic Sans MS'
    
    grid_kwargs={'color':white_hex,'linestyle':'--'}

def making_data():

    n_samples=1500
    random_state=100
    
    X,y=make_blobs(n_samples=n_samples,random_state=random_state)
    
    return X,y

def plotting(idx,X,y=None):
    
    fig=plt.figure(idx,figsize=(10,8))
    fig.patch.set_facecolor(Utils.black_hex)
    ax=fig.add_subplot(111)
    ax.scatter(X[:,0],X[:,1])
    ax.set_facecolor(Utils.black_hex)
    for spine in ax.spines.values():
        spine.set_edgecolor(Utils.white_hex)
        spine.set(linewidth=3)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.set_title('Clusters',color=Utils.purple_hex,
                     fontproperties={'family':Utils.csfont,'size':20})
    ax.tick_params(axis='x', colors=Utils.purple_hex,labelsize=15)
    ax.tick_params(axis='y', colors=Utils.purple_hex,labelsize=15)
    
    ax.grid(True,**Utils.grid_kwargs)
    

        
def saving(X,y):
    
    dat=pd.DataFrame(X,columns=['A','B'])
    dat['y_fact']=y
    
    dat.to_csv('../Data/clusters.csv')

def main():
    
    X,y=making_data()
    plotting(1,X)
    saving(X,y)

if __name__=="__main__":
    
    main()