#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np

#Computing cost_function
def compute_cost(x, y, w, b):
    m = len(x)
    total_cost = 0
    for i in range(m):
        prediction_c = (w * x[i]) + b    #Prediction
        cost = (prediction_c - y[i]) ** 2    #Individual cost
        total_cost += cost    #Summation of cost
    total_cost /= (2 * m)    #Average value of total_cost
    return total_cost

#Computing gradient_descent function
def compute_gradient(x, y, w, b):
    m = len(x)
    dw = 0
    db = 0
    for i in range(m):
        prediction_g = (w * x[i]) + b    #Prediction
        db += (prediction_c - y[i])    #Gradient for parameter b
        dw += (prediction_g - y[i]) * x[i]   #Gradient for parameter w
        
    #Total gradient update   
    db /= m
    dw /= m
    
    return dw,db

