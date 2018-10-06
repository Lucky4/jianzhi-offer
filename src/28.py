# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        
    def push(self, node):
        self.stack1.append(node)
        
        if len(self.stack2) == 0:
            self.stack2.append(node)
        elif node <= self.stack2[-1]:
            self.stack2.append(node)
        
    def pop(self):
        if self.stack1[-1] == self.stack2[-1]:
            self.stack2.pop()
        return self.stack1.pop()
    
    def top(self):
        return self.stack1[-1]
    
    def min(self):
        return self.stack2[-1]