# -*- coding: utf-8 -*-
"""
Created on Wed May 11 12:59:29 2022

@author: AVERKHO
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.close('all')

from utils import Utils


from sklearn.cluster import KMeans

def read_data():
    
    dat=pd.read_csv('../Data/clusters.csv')
    
    return dat


def plotting(idx,X,y=None):
    
    
        
    
    fig=plt.figure(idx,figsize=(10,8))
    fig.patch.set_facecolor(Utils.black_hex)
    ax=fig.add_subplot(111)
    if y is not None:
        
        color_list=[Utils.red_hex,Utils.green_hex,Utils.yellow_hex,Utils.blue_hex,Utils.white_hex]
        
        
        ax.scatter(X[:,0],X[:,1],c=y)
          
    else:
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
    

def kmeans(X,n_clusters=3):
    
    kmeans_clustering=KMeans(n_clusters=n_clusters)
    kmeans_clustering.fit(X)
    y_pred=kmeans_clustering.predict(X)
        
    return y_pred
    

def main():
    
    dat=read_data()
    X=dat[['A','B']].values
    y=dat['y_fact']
    plotting(1,X)
    
    y_pred=kmeans(X)
    
    plotting(2,X,y=y_pred)
    
    return y_pred
    
    

if __name__=="__main__":
    
    y_pred=main()