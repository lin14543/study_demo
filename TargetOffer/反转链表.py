# -*- coding:utf-8 -*-

'''
输入一个链表，反转链表后，输出新链表的表头。
'''

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        if not pHead:
            return
        flag_old = pHead
        new_list = ListNode(-1)
        while True:
            if not flag_old:
                break
            temp = flag_old
            flag_old = flag_old.next
            temp.next = new_list.next
            new_list.next = temp
        return new_list.next

