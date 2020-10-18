# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 16:35:40 2020

@author: crath
"""
# from sys import maxsize 
def contiSub(z,size):   
    max_total = 0
    max_curr = 0
    start_idx = 0
    end_idx = 0
    x = 0
  
    for i in range(0,size):   
        max_curr += z[i] # current value added to next value
  
        if max_total < max_curr: # current index value less than the total so far
            max_total = max_curr # total so far becomes the current value
            start_idx = x
            end_idx = i          # end is the current index value
        if max_curr < 0:         # current value is a negative value
            max_curr = 0         # current value becomes 0
            x = i+1              
  
    print ("Sum of maximum contiguous array is: %d"%(max_total)) 
    print ("Starts from index %d"%(start_idx) + " and ends with %d"%(end_idx)) 
    
z = [-4, -1, -4, 1, 5, -1, 4, -3] 
contiSub(z,len(z)) 

print("\n")
y = [-2, 1, -3, 4, -1, 2, 1, -5, 4] 
contiSub(y,len(y)) 