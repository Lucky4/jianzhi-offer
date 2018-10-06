# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        tmp = self.helper(listNode)
        res = []
        while tmp != None:
            res.append(tmp.val)
            tmp = tmp.next
        return res

    def helper(self, listNode):
        if listNode == None or listNode.next == None:
            return listNode
        
        new_head = self.helper(listNode.next)
        listNode.next.next = listNode
        listNode.next = None
        
        return new_head


# 可以使用栈。