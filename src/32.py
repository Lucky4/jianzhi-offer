# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def FindPath(self, root, expectNumber):
        res = []
        path = []
        self.helper(root, expectNumber, res, path)
        return res

    def helper(self, root, expectNumber, res, path):
        if root == None:
            return None
        
        path.append(root.val)
            
        if root.left == None and root.right == None and \
            sum(path) == expectNumber:
            res.append(path[:])

        if root.left != None:
            self.helper(root.left, expectNumber, res, path)
            
        if root.right != None:
            self.helper(root.right, expectNumber, res, path)

        path.pop()

    def helper2(self, root, expectNumber, res, path):
        '''
        路径的终点不一定是叶子节点。
        '''
        if root == None:
            return None
            
        path.append(root.val)
        
        if sum(path) == expectNumber:
            res.append(path[:])

        if root.left != None and sum(path) < expectNumber:
            self.helper(root.left, expectNumber, res, path)

        if root.right != None and sum(path) < expectNumber:
            self.helper(root.right, expectNumber, res, path)

        path.pop()