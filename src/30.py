# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque


class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print2(self, pRoot):
        res = []
        if pRoot == None:
            return res
        
        tmp_res = []
        q = deque()
        q.append(pRoot)
        start = 0
        end = 1

        while len(q) > 0:
            tmp = q.popleft()
            tmp_res.append(tmp.val)
            start += 1

            if tmp.left != None:
                q.append(tmp.left)

            if tmp.right != None:
                q.append(tmp.right)
                
            if start == end:
                res.append(tmp_res)
                tmp_res = []
                start = 0
                end = len(q)
                
        return res