# -*- coding:utf-8 -*-

'''
统计一个数字在排序数组中出现的次数。
'''


class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        return self.findIndex(data, k + 0.5) - self.findIndex(data, k - 0.5)

    def findIndex(self, data, k):
        left = 0
        right = len(data)
        while left < right:
            mid = (left + right) / 2
            flag = data[mid]
            if flag < k:
                left = mid + 1
            else:
                right = mid
        return right