# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 14:45:48 2022

@author: AVERKHO
"""

import numpy as np
import random
from tqdm import tqdm
#from overloading import overload
import typing

random.seed(1)


def perceptron_step(feature_vector,label,current_theta,current_theta_0=0):
    
    """
    Performance of a signgle step of the perceptron algorithm. 
    Updating of theta and theta_0, on a single step of the perceptron algorithm.

    Args:
        feature_vector - A numpy array describing a single data point.
        label - The correct classification of the feature vector.
        current_theta - The current theta being used by the perceptron
            algorithm before this update.
        current_theta_0 - The current theta_0 being used by the perceptron
            algorithm before this update.

    Returns: A tuple where the first element is a numpy array with the value of
    theta after the current update has completed and the second element is a
    real valued number with the value of theta_0 after the current updated has
    completed.
    """
    
    if label*(np.sum(np.dot(current_theta,feature_vector))+current_theta_0)<=0:
        return (current_theta+label*feature_vector,current_theta_0+label)
    
    return (current_theta,current_theta_0)


def perceptron(X,y,num_iterations):
    
    """
    Runs the full perceptron algorithm on a given set of data. Runs num_iterations
    iterations through the data set.

    Args:
        X -  A numpy matrix describing the given data. Each row
            represents a single data point.
        y - A numpy array where the kth element of the array is the
            correct classification of the kth row of the feature matrix.
        num_iterations - An integer indicating how many times the perceptron algorithm
            should iterate through the feature matrix.

    Returns: A tuple where the first element is a numpy array with the value of
    theta, the linear classification parameter, after num_iterations iterations through the
    feature matrix (X) and the second element is a real number with the value of
    theta_0, the offset classification parameter, after num_iterations iterations through
    the feature matrix (X).
    """
    
    current_theta=np.zeros((X.shape[1],))
    current_theta_0=0
    
    iteration_order=list(range(X.shape[0]))
    
    random.shuffle(iteration_order)
    print(iteration_order)
    
    for it in tqdm(range(num_iterations)):
        
        for i in iteration_order:
            
            feature_vector=X[i]
            label=y[i]
            
            current_theta,current_theta_0=perceptron_step(feature_vector,
                                                          label,
                                                          current_theta,
                                                          current_theta_0)
    return current_theta,current_theta_0
        
def perceptron_visualize(X,y,num_iterations,iteration_order,offset=True):
    
    theta=[]
    theta_0=[]
    
    current_theta=np.zeros((X.shape[1],))
    current_theta_0=0
    
    theta.append(current_theta)
    theta_0.append(current_theta_0)
     
    
    for it in tqdm(range(num_iterations)):
        
        for i in iteration_order:
            
            feature_vector=X[i]
            label=y[i]
            
            if offset:
                current_theta,current_theta_0=perceptron_step(feature_vector,
                                                              label,
                                                              current_theta,
                                                              current_theta_0)
                                                              
            else:
                current_theta,current_theta_0=perceptron_step(feature_vector,
                                                              label,
                                                              current_theta)
                            
                
            theta.append(current_theta)
            theta_0.append(current_theta_0)
            
    return theta,theta_0
    
    