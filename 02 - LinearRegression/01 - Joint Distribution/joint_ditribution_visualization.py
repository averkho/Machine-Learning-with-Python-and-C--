# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 16:22:11 2022

@author: AVERKHO
"""
import numpy as np
import matplotlib.pyplot as plt
plt.close('all')
import pandas as pd

from dataclasses import dataclass
import os
import shutil

path_to_3d_figures='./figures_3d/'
path_to_2d_figures='./figures_2d/'

if not os.path.exists(path_to_3d_figures):
    os.mkdir(path_to_3d_figures)
    
if not os.path.exists(path_to_2d_figures):
    os.mkdir(path_to_2d_figures)
    
from scipy.stats import multivariate_normal

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
    
    
random_seed=1000    
covariances=[0,0.5,0.8,0.99]
means=np.array([0,0])
pdf_list=[]

for idx,cov in enumerate(covariances):
    
    cov_matrix=np.array([[1,cov],[cov,1]])
    distribution=multivariate_normal(cov=cov_matrix,mean=means,seed=random_seed)
    
    x=np.linspace(-3*cov_matrix[0,0],3*cov_matrix[1,1],100)
    y=np.linspace(-3*cov_matrix[0,0],3*cov_matrix[1,1],100)
    
    X,Y=np.meshgrid(x,y)
    pdf=np.zeros(X.shape)
    
    for i in range(len(x)):
        
        for j in range(len(y)):
            
            pdf[i,j]=distribution.pdf([X[i,j],Y[i,j]])
    
    pdf_list.append(pdf)
    
    fig=plt.figure(idx,figsize=(10,10))
    fig.patch.set_facecolor(Utils.black_hex)
    ax=fig.add_subplot(111,projection='3d')
    ax.plot_surface(X,Y,pdf,cmap='viridis')
    ax.set_facecolor(Utils.black_hex)
    for spine in ax.spines.values():
        spine.set_edgecolor(Utils.white_hex)
        spine.set(linewidth=3)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.set_title('Covariance is {}'.format(cov),color=Utils.purple_hex,
                 fontproperties={'family':Utils.csfont,'size':20})
    ax.tick_params(axis='x', colors=Utils.purple_hex,labelsize=15)
    ax.tick_params(axis='y', colors=Utils.purple_hex,labelsize=15)
    ax.tick_params(axis='z', colors=Utils.purple_hex,labelsize=15)

for i in range(len(covariances)):
    
    idx+=1
    
    fig=plt.figure(idx,figsize=(10,10))
    fig.patch.set_facecolor(Utils.black_hex)
    ax=fig.add_subplot(111)
    ax.contourf(X,Y,pdf_list[i],cmap='viridis')
    ax.set_xlabel('x1',color=Utils.purple_hex,fontweight='bold',
                      fontproperties={'family':Utils.csfont,'size':20})
    ax.set_ylabel('x2',color=Utils.purple_hex,fontweight='bold',
                      fontproperties={'family':Utils.csfont,'size':20})
    
    ax.tick_params(axis='x', colors=Utils.purple_hex,labelsize=15)
    ax.tick_params(axis='y', colors=Utils.purple_hex,labelsize=15)
    ax.set_title('Covariance is {}'.format(covariances[i]),color=Utils.purple_hex,
                 fontproperties={'family':Utils.csfont,'size':20})
    
    plt.savefig(f'{path_to_2d_figures}{i}.png',dpi=400,transparent=True)
    
    
    
    

