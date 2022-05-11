# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 22:53:36 2022

@author: Alexander
"""

import torch
import torch.nn as nn
import numpy as np

np.random.seed(100)
torch.random.manual_seed(100)

X=np.random.random((10,10))
X_tensor=torch.Tensor(X)
X_tensor=torch.reshape(X_tensor,[1,1,10,10])

'''

PART I Conv2d(1,1)

'''
conv_layer=nn.Conv2d(1,1,kernel_size=2,stride=1,bias=False)
output=conv_layer(X_tensor)

output=torch.squeeze(output)
output=output.detach().cpu().numpy()

kernel=conv_layer.weight
kernel=torch.squeeze(kernel)
kernel=kernel.detach().cpu().numpy()

def convolution1to1(kernel,stride=1):
    
    m,n=X.shape
    k=len(kernel)
    
    dim=m-k+1
    
    Y=np.zeros((dim,dim))
    
    for i in range(0,dim,stride):
        
        for j in range(0,dim,stride):
            
            x=X[i:i+kernel.shape[0],j:j+kernel.shape[0]]
            Y[i,j]=np.sum(np.multiply(x,kernel))
    
    return Y

Y=convolution1to1(kernel,stride=1)

'''
PART II end

'''

conv_layer=nn.Conv2d(in_channels=1, out_channels=2, kernel_size=2,stride=1,bias=False)
output2=conv_layer(X_tensor)
output_to_normalize=output2
output2=torch.squeeze(output2)
output2=output2.detach().cpu().numpy()

kernel2=conv_layer.weight
kernel2=torch.squeeze(kernel2)
kernel2=kernel2.detach().cpu().numpy()

def convolution1x2(out_channels=2,kernel=kernel2,stride=1,padding=0):
    
    m,n=X.shape
    dim=X.shape[-1]-kernel.shape[-1]+1
    
    Y=np.zeros((out_channels,dim,dim))
    
    for channel in range(out_channels):
        
        for i in range(0,dim,stride):
            
            for j in range(0,dim,stride):
                
                x=X[i:i+kernel.shape[1],j:j+kernel.shape[2]]
                Y[channel,i,j]=np.sum(np.multiply(x,kernel[channel,:,:]))
                
    return Y

Y2=convolution1x2(out_channels=2,kernel=kernel2,stride=1,padding=0)

'''
PART IV

'''
             
X2=np.random.random((3,10,10))
X2_tensor=torch.Tensor(X2)
conv_layer=nn.Conv2d(in_channels=3,out_channels=9,kernel_size=2,stride=1,padding=0,bias=False)
out3=conv_layer(X2_tensor)
out3=out3.detach().cpu().numpy()
kernel3=conv_layer.weight
kernel3=torch.squeeze(kernel3)
kernel3=kernel3.detach().cpu().numpy()


batch_norm=nn.BatchNorm2d(num_features=2)
Y2_norm=batch_norm(output_to_normalize)
Y2_norm=torch.squeeze(Y2_norm)
Y2_norm=Y2_norm.detach().cpu().numpy()

def batch_normalization(X,eps=1e-5):
    
    dim=X.shape[0]
    Y=np.zeros(X.shape)
    for i in range(dim):
        
        x_mean=np.mean(X[i,:,:])
        x_var=np.var(X[i,:,:])
        Y=(X-x_mean)/np.sqrt(x_var+eps)
        print(x_var)
    
    return Y

Y=batch_normalization (Y2)  
    


        
    
    
