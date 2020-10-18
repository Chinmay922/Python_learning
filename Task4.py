# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 03:53:06 2020

@author: crath
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        dic = {}
        index_dic = 0 # current index position
        length = 0    # current length of the sub string
        longest = 0   # longest substring
        for i, letter in enumerate(s):               # enumerate to know the index position 
            if letter in dic and dic[letter] >= index_dic:  # to check if the current letter in dictonary and its index position
                index_dic = dic[letter] + 1                 # if yes then starting the check again from the index position of the previous seen letter +1 position
                length = i - dic[letter]                    # assigning the length to be the current index so to start from there rather than from the initial position
                dic[letter] = i                             # new start position
                
            else:
                dic[letter] = i                             # if false then continue with the current index position
                length += 1                                 # check next
                
                if length > longest:                        # assign the current length to be the longest 
                    longest = length 
                    
        return longest

out = Solution()
# substr = str(input("Enter sub string : "))
# print('For given Substring (', substr, ') the length of longesrt substring is, ')
print('The length of the longest substring without repeat is ', out.lengthOfLongestSubstring('abacdefff'))
print('\n')
print('The length of the longest substring without repeat is ', out.lengthOfLongestSubstring('abcabcbb'))
  
    
                
        