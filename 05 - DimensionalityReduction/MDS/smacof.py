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
    

