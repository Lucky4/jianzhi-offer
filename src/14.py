# -*- coding: utf-8 -*-
class Solution:
    def Power(self, base, exponent):
        if base == 0:
	        return False
        if exponent == 0:
	        return 1

        is_minus = False
        if exponent < 0:
	        is_minus = True
	        exponent = abs(exponent)

        curr = base
        res = 1
        while exponent != 0:
            if exponent & 1 == 1:
                res *= curr
                curr *= curr
                exponent >>= 1

        if is_minus:
            res = 1 / res
        return res

    # def Power(self, base, exponent):
    #     if base == 0:
    #         return False
    #     if exponent == 0:
    #         return 1

    #     is_minus = False
    #     if exponent < 0:
    #         is_minus = True
    #         exponent = abs(exponent)

    #     if exponent == 1: # 这部是处理奇数偶数的关键，运行到这里就返回了，没有继续执行下面的操作。
    #         return base

    #     res = self.Power(base, exponent >> 1)
    #     res *= res
    #     if exponent & 1 == 1:
    #         res *= base

    #     if is_minus:
    #         return 1 / res
    #     return res