# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 14:46:44 2022

@author: AVERKHO
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import multivariate_normal

plt.close('all')

random_seed=10000

covariance_val=[-0.8,0,0.99]

means=np.array([0,0])

pdf_list=[]

fig=plt.figure(figsize=[10,7])

for idx,val in enumerate(covariance_val):
    
    cov=np.array([[1,val],[val,1]])
    
    distr=multivariate_normal(cov=cov,mean=means,seed=random_seed)
    
    mean_1,mean_2=means[0],means[1]
    sigma_1,sigma_2=cov[0,0],cov[1,1]
    
    x=np.linspace(-3*sigma_1,3*sigma_1,num=100)
    y=np.linspace(-3*sigma_2,3*sigma_2,num=100)
    X,Y=np.meshgrid(x,y)
    
    pdf=np.zeros(X.shape)
    
    for i in range(X.shape[0]):
        for j in range(X.shape[1]):
            
            pdf[i,j]=distr.pdf([X[i,j],Y[i,j]])
    
    
    key=131+idx
    ax=fig.add_subplot(key,projection='3d')
    ax.plot_surface(X,Y,pdf,cmap='viridis')
    ax.set_xlabel('x1')
    ax.set_ylabel('x2')
    ax.set_title('Covariance between x1 and x2 is {}'.format(val))
    pdf_list.append(pdf)
    ax.axes.zaxis.set_ticks([])

plt.tight_layout()
plt.show()

fig=plt.figure(2)

for idx,val in enumerate(pdf_list):
    
    ax=fig.add_subplot(1,3,idx+1)
    ax.contourf(X,Y,val,cmap='viridis')
    plt.xlabel('x1')
    plt.ylabel('x2')
    plt.title('Covariance between x1 and x2 = {}'.format(covariance_val[idx]))
    

plt.tight_layout()
plt.show()
    
    