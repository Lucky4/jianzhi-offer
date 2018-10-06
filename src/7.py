# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
         
    def push(self, node):
        self.stack1.append(node)
         
    def pop(self):
        if self.is_empty(self.stack2):
            self.stack2 = self.stack1[::-1]
            self.stack1 = []
        return self.stack2.pop()
             
    def is_empty(self, stack):
        return len(stack) == 0