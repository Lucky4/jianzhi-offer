# -*- coding: utf-8 -*-
from ctypes import *


class NumberOf1(object):
    def NumberOf1(self, n):
        count = 0
        flag = 1

        while c_int(flag).value:
            if flag & n:
                count += 1
            flag = flag << 1 # 利用整数1左移与n的每个位相与

        return count

    # def NumberOf1(self, n):
    #     count = 0
    #     while c_int(n).value:
	#         count += 1
	#         n = (n -1 ) & n  # 把一个整数减去1，再和原整数做与运算，会把该整数最右边一个1变成0
    #     return count


# 注意：Python没有数据类型，左移或右移越位之后会自动将int转为long类型。可以在Python中调用C语言。