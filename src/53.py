# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def TreeDepth(self, pRoot):
        if pRoot == None:
            return 0

        left = self.TreeDepth(pRoot.left)+1
        right = self.TreeDepth(pRoot.right)+1
        
        return max(left, right)