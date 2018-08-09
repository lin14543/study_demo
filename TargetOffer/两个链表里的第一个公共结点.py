# -*- coding:utf-8 -*-

'''
输入两个链表，找出它们的第一个公共结点。
'''

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        len1 = self.GetLength(pHead1)
        len2 = self.GetLength(pHead2)
        diff = len1 - len2
        if diff >= 0:
            lon = pHead1
            short = pHead2
        else:
            lon = pHead2
            short = pHead1
            diff = - diff
        for i in range(diff):
            if lon:
                lon = lon.next
            else:
                return
        while lon or short:
            if lon == short:
                return lon
            lon = lon.next
            short = short.next
        return None

    def GetLength(self, pHead1):
        if not pHead1:
            return 0
        flag = pHead1
        sum = 0
        while flag:
            flag = flag.next
            sum += 1
        return sum