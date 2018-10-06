# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        res = False
        
        if pRoot1 != None and pRoot2 != None:
            if pRoot1.val == pRoot2.val:
                res = self.DoesTree1HaveTree2(pRoot1, pRoot2)
        
            if not res:
                res = self.HasSubtree(pRoot1.left, pRoot2)
        
            if not res:
                res = self.HasSubtree(pRoot1.right, pRoot2)
        
        return res
        
    def DoesTree1HaveTree2(self, pRoot1, pRoot2):
        if pRoot2 == None:
            return True
        
        if pRoot1 == None and pRoot2 != None:
            return False
        
        if pRoot1.val != pRoot2.val:
            return False
        
        return self.DoesTree1HaveTree2(pRoot1.left, pRoot2.left) and \
            self.DoesTree1HaveTree2(pRoot1.right, pRoot2.right)