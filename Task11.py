# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 12:03:20 2020

@author: crath
"""


  
import numpy as np
x = np.array([[0, 10, 20], [20, 30, 40]])            # to create a numpy array
y = x[x>10]                                          # to give all the values greater than 10
z1 = np.argwhere(x[0] > 10)                          # indexing of all the values whihc are non zero and greater than 10
z2 = np.argwhere(x[1] > 10)
# w = np.argwhere(x[0]>10), np.argwhere(x[1]>10)    
print("Original array: \n", + x)                     # print original array
print("Value bigger than x: \n", y)                  # print numbers in the array bigger than 10
print("Indices of the values of array x[0]: \n", z1, '\n') # print the index of number greater than 10
print("Indices of the values of array x[1]: \n", z2)
       