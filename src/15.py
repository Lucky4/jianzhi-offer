# -*- coding:utf-8 -*-
class Solution:
    def func(self, n):
        if n <= 0:
            return None
        
        number = [0] * n

        for i in range(10):
            number[0] = i
            self.helper(number, n, 0)

    def helper(self, number, length, index):
        if index == length - 1:
            self.printNumber(number)
            return None

        for i in range(10):
            number[index+1] = i
            self.helper(number, length, index+1)

    def printNumber(self, number):
        begin_0 = True

        for i in range(len(number)):
            if begin_0 and number[i] != 0:
                begin_0 = False

            if not begin_0:
                print number[i]

        print '\t'