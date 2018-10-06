# -*- coding:utf-8 -*-
class Solution:
    def LastRemaining_Solution(self, n, m):
        if n < 1 or m < 1:
            return -1

        last = 0

        for i in range(2, n + 1):
            last = (last + m) % i

        return last


# 本题实际上就是约瑟夫环问题,记住公式:
#                  0         , n = 1
# f(n, m)= [f(n-1, m)+m] % n , n > 1
#
# 参考: http://zhedahht.blog.163.com/blog/static/2541117420072250322938/