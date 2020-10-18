# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 03:52:18 2020

@author: crath
"""

class TreeNode(object):
    """ Definition of a binary tree node."""
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
def solution(root):
    if root is None:                              # If root not found then return none
        return False;
    else:
        
        left_depth = solution(root.left)          # find the depth of the left stem
        right_depth =solution(root.right)         # find the depth of the right stem
        depth = 1 + max(left_depth, right_depth)  # return the maximum depth between left and right
    return depth

a15=TreeNode(15)
a7=TreeNode(7)
a20=TreeNode(20)
a9=TreeNode(9)
a3=TreeNode(3)
a20.left=a15
a20.right=a7
a3.left=a9
a3.right=a20
a1 = TreeNode(1)
a55=TreeNode(55)
print('Max depth of the given binary tree: ', solution(a3))

a15=TreeNode(15)
a7=TreeNode(7)
a20=TreeNode(20)
a9=TreeNode(9)
a3=TreeNode(3)
a5= TreeNode(5)
a8 = TreeNode(8)
a20.left=a15
a20.right=a7
a3.left=a9
a3.right=a20
a15.left=a5
a15.right=a8
print('Max depth of the given binary tree: ', solution(a3))


