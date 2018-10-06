# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        array_length = len(rotateArray)
        if array_length == 0:
            return 0
        
        l = 0
        h = array_length - 1
        m = 0
        
        while rotateArray[l] >= rotateArray[h]:
            if h - l == 1:
                m = h
                break
                
            m = (l + h) / 2

            if rotateArray[m] >= rotateArray[l]:
                l = m

            if rotateArray[m] <= rotateArray[h]:
                h = m
        
        return rotateArray[m]
