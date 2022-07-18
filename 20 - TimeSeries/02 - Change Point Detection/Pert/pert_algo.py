# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 11:19:02 2022

@author: AVERKHO
"""
import numpy as np
import matplotlib.pylab as plt
import ruptures as rpt
import pandas as pd
from math import floor

plt.close('all')

dat = pd.read_csv('data.csv')

# change point detection
model = "l1"  # "l2", "rbf"

algo = rpt.Pelt(model = model, min_size = 300, jump = 10).fit(dat['level'].values)
pert_pred = algo.predict(pen = 3)

fig = plt.figure(2)
ax = fig.add_subplot(111)
ax.plot(dat['level'])
for line in pert_pred:
    ax.axvline(line,color = 'red', linestyle = '--')
    
 


partitions = dict()  # this dict will be recursively filled
partitions[0] = {(0, 0): 0}
admissible = []

n_samples = dat.shape[0]
jump = 10
min_size = 300
pen = 3

signal = dat['level'].values

def error(start,end):
    
    if end - start < min_size:
        return
    sub = signal[start:end]
    med = np.median(sub, axis=0)

    return abs(sub - med).sum()
    
 # Recursion
ind = [k for k in range(0, n_samples, jump) if k >= min_size]
ind += [n_samples]
for bkp in ind:
    # adding a point to the admissible set from the previous loop.
    new_adm_pt = floor((bkp - min_size) / jump)
    new_adm_pt *= jump
    admissible.append(new_adm_pt)

    subproblems = list()
    for t in admissible:
                # left partition
        try:
            tmp_partition = partitions[t].copy()
        except KeyError:  # no partition of 0:t exists
            continue
                # we update with the right partition
        tmp_partition.update({(t, bkp): error(t, bkp) + pen})
        subproblems.append(tmp_partition)

    # finding the optimal partition
    partitions[bkp] = min(subproblems, key=lambda d: sum(d.values()))
    # trimming the admissible set
    admissible = [
                t
                for t, partition in zip(admissible, subproblems)
                if sum(partition.values()) <= sum(partitions[bkp].values()) + pen
            ]

best_partition = partitions[n_samples]
bkps = sorted(e for s, e in best_partition.keys())
del best_partition[(0, 0)]