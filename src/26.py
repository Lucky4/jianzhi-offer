# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def isSymmetrical(self, pRoot):
        if pRoot == None:
            return True
            
        return self.f(pRoot.left, pRoot.right)
    
    def helper(self, t1, t2):
        if not t1 and not t2:
            return True

        if not t1 and t2:
            return False

        if not t2 and t1:
            return False

        if t1 and t2 and t1.val != t2.val:
            return False

        return self.helper(t1.left, t2.right) and self.helper(t1.right, t2.left)