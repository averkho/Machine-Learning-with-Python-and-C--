# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 11:43:54 2022

@author: AVERKHO
"""

from sklearn.linear_model import LinearRegression

import numpy as np

A=np.array([[1, 2, 3, 4],[1, 2, 3 ,4],[2,3,4,5]])
y=np.array([1,2,3])

y=np.transpose(y)

lr=LinearRegression()

lr.fit(A,y)

pred=lr.predict(A)

x, residuals, rank, s=np.linalg.lstsq(A,y)

coefficients=lr.coef_