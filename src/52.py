# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        if pRoot == None or k == 0:
            return None
         
        count = [k]

        return self.KthNodeCore(pRoot, count)
         
    def KthNodeCore(self, pRoot, k):
        if pRoot == None:
            return None
            
        target = None
         
        if pRoot.left != None:
            target = self.KthNodeCore(pRoot.left, k)
             
        if target == None:
            if k[0] == 1:
                target = pRoot
            k[0] -= 1
         
        if target == None and pRoot.right != None:
            target = self.KthNodeCore(pRoot.right, k)
             
        return target