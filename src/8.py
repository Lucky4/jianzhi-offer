# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        if n < 2:
            return n

        first = 0
        second = 1
        third = 0
        count = 2

        while count <= n:
            third = first + second
            first = second
            second = third
            count += 1

        return third