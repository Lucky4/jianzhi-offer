# -*- coding: utf-8 -*-
class Solution(object):
    def MoreThanHalfNumSolution(self, numbers):
        more_half_number = numbers[0]
        times = 1

        for i in numbers[1:]:
            if i == more_half_number:
                times += 1
            elif times == 0:
                more_half_number = i
                times = 1
            else:
                times -= 1
        
        times = 0

        for j in numbers:
            if j == more_half_number:
                times += 1
                
        if times > len(numbers) / 2:
            return more_half_number

        return 0