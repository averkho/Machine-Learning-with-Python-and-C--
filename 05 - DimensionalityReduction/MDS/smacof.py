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
        max_iter = 300,
        ):
    
    

def smacof(dissimilarities,
           metric = True,
           n_components = 2,
           n_init = 8,
           max_iter = 300,
           ):
    
    best_stress,best_pos = None, None
    for i in range(n_init):
        pos,stress,n_iter_ = _smacof_single(
            dissimilarities,
            metric = metric,
            n_components = n_components,
            max_iter = max_iter,
            )
        if best_stress is None or stress < best_stress:
            
            best_stress = stress
            best_pos = pos.copy()
            best_iter = n_iter_
            
            
class MDS():
    
    
    def __init__(
            self,
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
        self.n_init = n_init,
        self.max_iter = max_iter,
        self.verbose = verbose,
        self.eps = eps,
        self.n_jobs = n_jobs,
        self.random_state = random_state
        self.dissimilarity = dissimilarity
        
        
    def fit(self, X, y=None, init=None):
        
        self.fit_transform(X, init=init)
        
    def fit_transform(self, X, y=None, init=None):
        
        if self.dissimilarity == ""
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

