# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 18:20:34 2020

@author: crath
"""

#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: [ListNode]) -> ListNode:
        
        self.node = []
        extra = head = ListNode(0)
        for len in lists:
            while len:
                self.node.append(len.val)
                len = len.next
        sortedarr=sorted(self.node)        
        for x in sortedarr:
             extra.next = ListNode(x)
             extra = extra.next
        return head.next

if __name__ == '__main__':
        list1=ListNode(2)
        list1.next= ListNode(4)
        list1.next.next= ListNode(8)
        list2=ListNode(5)
        list2.next= ListNode(6)
        list2.next.next= ListNode(7)
        sorted_array=[list1, list2]
        solution1 = Solution().mergeKLists(sorted_array)
        print('Sorted LL is as: ')
        print(solution1.val)
        print(solution1.next.val)
        print(solution1.next.next.val)
        print(solution1.next.next.next.val)
        print(solution1.next.next.next.next.val)
        print(solution1.next.next.next.next.next.val)  
                                    
        