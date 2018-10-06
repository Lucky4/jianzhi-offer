# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        root = self.helper(pre, 0, len(pre)-1, tin, 0, len(tin)-1)
        return root
    
    def helper(self, pre, startPre, endPre, tin, startIn, endIn):
        if startPre > endPre or startIn > endIn:
            return None
        
        root = TreeNode(pre[startPre])
        
        for i in range(startIn, endIn+1):
            if tin[i] == pre[startPre]:
                root.left = self.helper(pre, startPre+1, startPre+i-startIn, tin, startIn, i-1)
                root.right = self.helper(pre, startPre+i-startIn+1, endPre, tin, i+1, endIn)
                break
        
        return root