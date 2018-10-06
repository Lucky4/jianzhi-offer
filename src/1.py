# -*- coding:utf-8 -*-
class Solution:
    def duplicate(self, numbers, duplication):
        numbers_count = len(numbers)
        status = [False] * numbers_count

        for i in range(0, numbers_count):
            if status[numbers[i]] == True:
                duplication[0] = numbers[i]
                return True
            status[numbers[i]] = True

        return False