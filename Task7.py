# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 03:53:07 2020

@author: crath
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root == None:
            return False
                                            
        if root.val == sum:            
            if root.left == None and root.right == None:                
                return True
            else:
                return self.hasPathSum(root.left, 0) or self.hasPathSum(root.right, 0)                 
        else:
            remain = sum - root.val
            return self.hasPathSum(root.left , remain) or self.hasPathSum(root.right, remain)

a15=TreeNode(15)
a7=TreeNode(7)
a20=TreeNode(20)
a9=TreeNode(9)
a3=TreeNode(3)
a1=TreeNode(131)
a20.left=a15
a20.right=a7
a3.left=a9
a3.right=a20
a7.right = a1
number = int(input("Enter a number : "))
print(Solution().hasPathSum(a3, number))
      