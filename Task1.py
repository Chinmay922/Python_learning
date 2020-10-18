# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 03:52:18 2020

@author: crath
"""

# Time Optimed O(n)
def solution(list, target): 
    a=0                                                    # initializing the value of a 
    b=0                                                    # initializing the value of b     
    for i in list:
        a= i
        b = target-i
        if b in list:
            print(target, 'is the given sum for which the two Numbers in the List are: ') # printing the two numbers in the list
            return a,b                                     # returning the value of a and b
        
target = int(input("Enter first number: "))                # Enter the desired sum
numbers = [2, 7, 11, 4, 8, 10, 13]                         # array of numbers
print(solution(numbers, target), '\n')
target = int(input("Enter second number: "))                            
numbers = [2, 4, 7, 11]                                    # array of numbers
print(solution(numbers, target)) 