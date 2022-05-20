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



class PCA_calc():
    
    def __init__(self,dat,n_components=None):
        
        self.dat=dat
        
        if n_components is None:
            
            self.n_components=dat.shape[1]
        
        else:
            
            self.n_components=n_components
        
        
    def __scaling__(self):
        
        scaler=StandardScaler()
        self.X=scaler.fit_transform(self.dat)
    
    def __decompose__(self):
        
        '''
        
        Covariance matric computing and its eigenvalues decomposition
        
        '''
        
        X_cov=np.cov(self.X.T)

        self.W,self.V=np.linalg.eig(X_cov)

        self.D=np.diag(self.W)

        '''
        eigenvalues decomposition
        
        C = V x W x V.T
        
        '''

        C=np.matmul(np.matmul(self.V,self.D),self.V.T)
    
        
        
    def fit(self):
        
        self.__scaling__()
        self.__decompose__()

    def score_plot(self):

        '''
        
        Score plot calculation X * V
        
        '''
        self.T=np.matmul(self.X,self.V)
        
        fig=plt.figure(1,figsize=(10,8))
        ax=fig.add_subplot(111)
        ax.scatter(self.T[:,0],self.T[:,1],s=100,color=Utils.red_hex)
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
        for i in range(self.T.shape[0]):
            
            ax.text(self.T[i][0],self.T[i][1]+0.1,str(i),color=Utils.purple_hex)    
            
        plt.tight_layout()
    
    def loading_plot(self):

        '''
        
        Loading plot
        
        '''
        
        fig=plt.figure(2,figsize=(10,8))
        ax=fig.add_subplot(111)
        ax.scatter(self.V[:,0],self.V[:,1],s=100,color=Utils.red_hex)
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
        
        for i in range(self.T.shape[1]):
            
            ax.text(self.V[i][0],self.V[i][1]+0.01,self.dat.columns[i],color=Utils.purple_hex,size=14)    
            
        plt.tight_layout()
        
    
    def scree_plot(self):

        '''
        Scree plot
        
        '''
        
        fig=plt.figure(3,figsize=(10,8))
        ax=fig.add_subplot(111)
        box=ax.bar(np.arange(len(self.W)),self.W)
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

def main():
    
    dat=pd.read_excel('./Credit score.xlsx')

    pca_=PCA_calc(dat)
    pca_.fit()
    pca_.score_plot()
    pca_.loading_plot()
    pca_.scree_plot()
    
    
    

if __name__=="__main__":
    
    main()


