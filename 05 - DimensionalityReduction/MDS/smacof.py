#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 21:10:54 2022

@author: alexander
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.close('all')
from sklearn.metrics import pairwise_distances

dat = pd.read_csv('./Data/mds_data.csv')

X = np.array(dat[['x1', 'x2', 'x3']])
D = pairwise_distances(X)

def _smacof_single(
        dissimilarities,
        metric = True,
        n_components = 2,
        init = None,
        max_iter = 300,
        verbose = 0,
        eps = 1e-3,
        random_state = None,
        ):
    
    old_stress = None
    n_samples = dissimilarities.shape[0]
    
    if init is None:
        
        X = np.random.uniform(size = n_samples * n_components)
        X = X.reshape((n_samples,n_components))
    
    for it in range(max_iter):
        
        dis = pairwise_distances(X)
        
        if metric:
            
            disparities = dissimilarities
        
        else:
            pass
        
        
        #Stress computing
        stress = ((dis.ravel() - disparities.ravel())**2).sum() / 2
        
        # Update X using the Guttman transform
        dis[dis == 0] = 1e-5
        ratio = disparities / dis
        B = -ratio
        B[np.arange(len(B)),np.arange(len(B))] += ratio.sum()
        X = 1.0 / n_samples * np.dot(B,X)
        
        assert(1/0)
    

def smacof(dissimilarities,
           *,
           metric = True,
           n_components = 2,
           init = None,
           n_init = 8,
           n_jobs = None,
           max_iter = 300,
           verbose = 0,
           eps = 1e-3,
           random_state = None,
           return_n_iter = False,
           ):
        
    best_stress,best_pos = None, None
    
    for i in range(n_init):
        pos,stress,n_iter_ = _smacof_single(
            dissimilarities,
            metric = metric,
            n_components = n_components,
            init = init,
            max_iter = max_iter,
            verbose = verbose,
            eps = eps,
            random_state = random_state,
            )
        if best_stress is None or stress < best_stress:
            
            best_stress = stress
            best_pos = pos.copy()
            best_iter = n_iter_
            
            
class MDS():
    
    
    def __init__(
            self,
            n_components = 2,
            metric = True,
            n_init=4,
            max_iter = 300,
            verbose = 0,
            eps = 1e-3,
            n_jobs = None,
            random_state = None,
            dissimilarity = "euclidean"
            ):
        
        self.metric = metric
        self.n_init = n_init
        self.max_iter = max_iter
        self.verbose = verbose
        self.eps = eps
        self.n_jobs = n_jobs
        self.random_state = random_state
        self.dissimilarity = dissimilarity
        self.n_components = n_components
        
        
    def fit(self, X, y=None, init=None):
        
        self.fit_transform(X, init=init)
        
        return self
        
    def fit_transform(self, X, y=None, init=None):
        
        if self.dissimilarity == "precomputed":
            self.dissimilarity_matrix_ = X
        elif self.dissimilarity == "euclidean":
            self.dissimilarity_matrix_ = pairwise_distances(X)
        else:
            assert(1/0)
        
        self.emdedding_,self.stress_,self.n_iter_ = smacof(
            self.dissimilarity_matrix_,
            metric = self.metric,
            n_components = self.n_components,
            init = init,
            n_init = self.n_init,
            n_jobs = self.n_jobs,
            max_iter = self.max_iter,
            verbose = self.verbose,
            eps = self.eps,
            random_state = self.random_state,
            return_n_iter = True,
            )
        
        return self
    

mds = MDS()

mds.fit_transform(X)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

