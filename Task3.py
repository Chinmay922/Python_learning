# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 03:52:16 2020

@author: crath
"""
import math
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution():
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        empty = ListNode(0)    # dummy node
        current = empty        # current index to be 0
        carryon = 0            # current carryon
        while l1 or l2 :
            value1 = l1.val if l1 else 0 
            value2 = l2.val if l2 else 0
            
            
            output = value1 + value2 + carryon 
            carryon = math.floor(output/10)
            output=output%10
            
            current.val = output
            current.next = ListNode(0)
            current = current.next
                       
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        if (carryon>0):
            current.next = ListNode(carryon)
        
        return empty
 
if __name__ == '__main__':
        list1=ListNode(2)
        list1.next= ListNode(4)
        list1.next.next= ListNode(3)
        list2=ListNode(5)
        list2.next= ListNode(6)
        list2.next.next= ListNode(4)
        solution1 = Solution().addTwoNumbers(list2, list1)
        print('Given LList 1 + LList 2: ', '(2 -> 4 -> 3) + (5 -> 6 -> 4))')
        print(solution1.val, '->', solution1.next.val, '->',solution1.next.next.val )
        print(solution1.val)
        print(solution1.next.val)
        print(solution1.next.next.val)
        print('The outcome this is : ', solution1.next.next.val, solution1.next.val, solution1.val)
        
        print("\n \n") 
        list1=ListNode(9)
        list1.next= ListNode(9)
        list1.next.next= ListNode(4)
        list2=ListNode(1)
        list2.next= ListNode(2)
        list2.next.next= ListNode(3)
        solution1 = Solution().addTwoNumbers(list2, list1)
        print('Given LList 1 + LList 2: ', '(9 -> 9 -> 4) + (1 -> 2 -> 3))')
        print(solution1.val, '->', solution1.next.val, '->',solution1.next.next.val)
        print(solution1.val)
        print(solution1.next.val)
        print(solution1.next.next.val)
        print('The outcome this is : ', solution1.next.next.val, solution1.next.val, solution1.val)