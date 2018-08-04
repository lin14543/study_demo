# -*- coding:utf-8 -*-

'''
输入一个链表，输出该链表中倒数第k个结点。

需要注意的是当链表为空，k为0，还有k大于链表长度的时候
'''



# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        if not head or not k:
            return None
        flag_st = head
        flag_en = head
        for i in range(k):
            if not flag_en:
                return None
            flag_en = flag_en.next
        while True:
            if not flag_en:
                return flag_st
            flag_en = flag_en.next
            flag_st = flag_st.next