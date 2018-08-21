# -*- coding:utf-8 -*-
'''
题目描述:
    在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，重复的结点不保留，返回链表头指针。
    例如，链表1->2->3->3->4->4->5 处理后为 1->2->5
思路：
    用一个指针指向前一个节点，另一个指针指向正在遍历的节点，然后判断是否有重复的，有重复的就跳过即可。
'''
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:

    '''
    time: 30ms
    memory: 5728k
    '''

    def deleteDuplication(self, pHead):
        # write code here
        ans = ListNode(-1)
        ans.next = pHead
        p = pHead
        pre = ans
        while p and p.next:
            _next = p.next
            if p.val == _next.val:
                while _next and p.val == _next.val:
                    _next = _next.next
                pre.next = _next
            else:
                pre = p
            p = _next
        return ans.next
