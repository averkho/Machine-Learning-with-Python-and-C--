
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 15:43:54 2022

@author: AVERKHO
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from matplotlib import cm
import random
import os
import shutil
from typing import NamedTuple

from dataclasses import dataclass, field
from PIL import ImageColor
from matplotlib.animation import FuncAnimation


random.seed(1)

import sentiment_algorithms as algorithms 


#plt.close('all')

centers=[(-1,1),(2,4)]
feature_matrix,labels=make_blobs(20,2,centers=centers,cluster_std=[1.5,1.5],random_state=1)
y_unique=np.unique(labels)
#labels = list(labels)
#Utils=['red' for label in labels if label==1 else 'blue']
labels=np.where(labels==0,-1,1)


i=0
plt.close('all')
path_to_figures='./figures/'
shutil.rmtree(path_to_figures, ignore_errors=True)
os.mkdir(path_to_figures)

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
      

Utils.csfont
colors=list(np.where(labels==1,Utils.red_hex,Utils.blue_hex))

class BasePlotting():
    
    def __init__(self):
        
        if self.rendering:
        
            self.axes_color_hex=Utils.white_hex
            self.axes_color_rgba=Utils.white_rgba
    
        else:
        
            self.axes_color_hex=Utils.black_hex
            self.axes_color_rgba=Utils.black_rgba
    
    def set_style(self,ax,arrows=True,ticks=True,grid=True):
               
        
        for spine in ax.spines.values():
            spine.set_edgecolor(self.axes_color_hex)
            spine.set(linewidth=3)
        
        ax.spines['right'].set_visible(False)
        ax.spines['top'].set_visible(False)
        ax.set_xlabel('x1', labelpad=-24, x=1.07,
                      color=Utils.purple_hex,fontweight='bold',
                      fontproperties={'family':Utils.csfont,'size':20})
        ax.set_ylabel('x2', labelpad=-21, y=1.02, rotation=0,
                      color=Utils.purple_hex,fontweight='bold',
                      fontproperties={'family':Utils.csfont,'size':20})
        if arrows:
            arrow_fmt = dict(markersize=10, color=self.axes_color_rgba, clip_on=False)
            ax.plot((1), (0), marker='>', transform=ax.get_yaxis_transform(), **arrow_fmt)
            ax.plot((0), (1), marker='^', transform=ax.get_xaxis_transform(), **arrow_fmt)
        
        if not(ticks):
            ax.set_xticks([])
            ax.set_yticks([])
        ax.grid(grid)
    
    
        
class Plotting(BasePlotting):

    def __init__(self,saving=False,rendering=False):
        
        self.rendering=rendering
        super().__init__()
        
        self.saving=saving
    
    

    def plotting(self,fig,i,arrows=False,ticks=True,grid=True,saving=False):
        
        pass
        
        
        #fig=plt.figure(i+1)
        
        ax=fig.add_subplot(111)
        ax.scatter(feature_matrix[:,0],feature_matrix[:,1],color=colors)
        ax.spines['bottom'].set_position('zero')
        ax.spines['left'].set_position('zero')
        
        self.set_style(ax,arrows,ticks,grid,saving)
        
        '''
        for spine in ax.spines.values():
            spine.set_edgecolor(self.axes_color_hex)
            spine.set(linewidth=3)
        ax.spines['right'].set_visible(False)
        ax.spines['top'].set_visible(False)
        ax.set_xlabel('x1', labelpad=-24, x=1.07,
                      color=Utils.purple_hex,fontweight='bold',
                      fontproperties={'family':Utils.csfont,'size':20})
        ax.set_ylabel('x2', labelpad=-21, y=1.02, rotation=0,
                      color=Utils.purple_hex,fontweight='bold',
                      fontproperties={'family':Utils.csfont,'size':20})
        arrow_fmt = dict(markersize=10, color=self.axes_color_rgba, clip_on=False)
        ax.plot((1), (0), marker='>', transform=ax.get_yaxis_transform(), **arrow_fmt)
        ax.plot((0), (1), marker='^', transform=ax.get_xaxis_transform(), **arrow_fmt)
        ax.set_xticks([])
        ax.set_yticks([])
        ax.grid(True)
        
        
        if start:
            ax.set_title('Iteration = {}'.format(i-1),color=Utils.purple_hex,size=20,weight='bold')
            ax.plot(x,y,'-',lw=3,color=Utils.yellow_hex)
        '''   
        if saving:  
        
            plt.savefig('{}{}.png'.format(path_to_figures,i+1),dpi=400,transparent=True)
        
        
        
    def two_line_plotting(self,i,dat,col1,col2,arrows=False,grid=True):
            
        fig=plt.figure(i)
        ax=fig.add_subplot(111)
        ax.plot(dat[col1])
        ax.plot(dat[col2])
        
        self.set_style(ax,arrows,grid)
            
            
            
    
 
plotting=Plotting(rendering=False)



def plotting(i,x,y,pos_x,pos_y,start=False,rendering=False,saving=False):
    
    circle=plt.Circle((pos_x,pos_y),0.2,color=Utils.yellow_hex)
    
    
    fig=plt.figure(i+1)
            
    ax=fig.add_subplot(111)
    ax.scatter(feature_matrix[:,0],feature_matrix[:,1],color=colors)
    ax.spines['bottom'].set_position('zero')
    ax.spines['left'].set_position('zero')
    
    if rendering:
            
        axes_color_hex=Utils.white_hex
        axes_color_rgba=Utils.white_rgba
        
    else:
            
        axes_color_hex=Utils.black_hex
        axes_color_rgba=Utils.black_rgba      
    
            
            
    for spine in ax.spines.values():
        spine.set_edgecolor(axes_color_hex)
        spine.set(linewidth=3)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.set_xlabel('x1', labelpad=-24, x=1.07,
                  color=Utils.purple_hex,fontweight='bold',
                  fontproperties={'family':Utils.csfont,'size':20})
    ax.set_ylabel('x2', labelpad=-21, y=1.02, rotation=0,
                  color=Utils.purple_hex,fontweight='bold',
                  fontproperties={'family':Utils.csfont,'size':20})
    arrow_fmt = dict(markersize=10, color=axes_color_rgba, clip_on=False)
    ax.plot((1), (0), marker='>', transform=ax.get_yaxis_transform(), **arrow_fmt)
    ax.plot((0), (1), marker='^', transform=ax.get_xaxis_transform(), **arrow_fmt)
    ax.set_xticks([])
    ax.set_yticks([])
    
    ax.add_patch(circle)
    
    ax.grid(True)
            
            
    if start:
        ax.set_title('Iteration = {}'.format(i),color=Utils.purple_hex,size=20,weight='bold',
                     loc='right')
        ax.plot(x,y,'-',lw=3,color=Utils.yellow_hex)
    
             
    if saving:  
            
        plt.savefig('{}{}.png'.format(path_to_figures,i+1),dpi=400,transparent=True)





random.seed(2022)

iteration_order=list(range(feature_matrix.shape[0]))

random.shuffle(iteration_order)

num_iterations=4

theta,theta_0=algorithms.perceptron_visualize(feature_matrix,
                                              labels,
                                              num_iterations=num_iterations,
                                              iteration_order=iteration_order,offset=True)

theta_df=pd.DataFrame(theta,columns=['theta_1','theta_2'])

theta_0_df=pd.DataFrame(theta_0,columns=['theta_0'])

theta_df['position']=[-1]+num_iterations*iteration_order
'''

fig=plt.figure(theta_df.shape[0])
ax=fig.add_subplot(111)
ax.plot(theta_df['theta_1'])
ax.plot(theta_df['theta_2'])
ax.set_title('Parameter vector theta',fontproperties={'family':Utils.csfont,'size':17})
'''
 
    

for i in range(theta_df.shape[0]):
    
    
    theta=theta_df.loc[i]
    if theta_df.iloc[i]['position']!=-1:
        pos_x=feature_matrix[int(theta_df.iloc[i]['position'])][0] 
        pos_y=feature_matrix[int(theta_df.iloc[i]['position'])][1]
    else:
        pos_x,pos_y=0,0

    x=np.linspace(-2,4,100)
    y=(-theta[0]*x-theta_0[i])/theta[1]
    plotting(i,x,y,pos_x,pos_y,start=True,saving=True)
    
plt.close('all')
fig=plt.figure(1)
ax=fig.add_subplot(111)
ax.plot(theta_df['theta_1'],label='theta_1',color=Utils.green_hex,lw=4)
ax.plot(theta_df['theta_2'],label='theta_2',color=Utils.blue_hex,lw=4)

ax.set_xlabel('# of iterations',color=Utils.purple_hex,fontweight='bold',
                  fontproperties={'family':Utils.csfont,'size':20})

ax.set_ylabel('theta',color=Utils.purple_hex,fontweight='bold',
                  fontproperties={'family':Utils.csfont,'size':20})
ax.legend()
for spine in ax.spines.values():
    spine.set_edgecolor(Utils.black_hex)
    spine.set(linewidth=3)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.tick_params(axis='x', colors=Utils.purple_hex,labelsize=15)
ax.tick_params(axis='y', colors=Utils.purple_hex,labelsize=15)
plt.savefig('{}1.png'.format('./figures_2/'),dpi=400,transparent=True)


fig=plt.figure(2)
ax=fig.add_subplot(111)
ax.plot(theta_0_df['theta_0'],color=Utils.green_hex,lw=4)


ax.set_xlabel('# of iterations',color=Utils.purple_hex,fontweight='bold',
                  fontproperties={'family':Utils.csfont,'size':20})

ax.set_ylabel('theta 0',color=Utils.purple_hex,fontweight='bold',
                  fontproperties={'family':Utils.csfont,'size':20})
ax.legend()
for spine in ax.spines.values():
    spine.set_edgecolor(Utils.black_hex)
    spine.set(linewidth=3)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.tick_params(axis='x', colors=Utils.purple_hex,labelsize=15)
ax.tick_params(axis='y', colors=Utils.purple_hex,labelsize=15)
plt.savefig('{}2.png'.format('./figures_2/'),dpi=400,transparent=True)

def saving():
    dat_to_save=pd.DataFrame(feature_matrix,columns=['x1','x2'])
    dat_to_save['labels']=labels
    dat_to_save.to_csv('../02 - Cpp perceptron/data/toy.csv',index=False)
