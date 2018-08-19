# -*- coding:utf-8 -*-

'''
题目描述：
    输入一个复杂链表（每个节点中有节点值，以及两个指针，一个指向下一个节点，另一个特殊指针指向任意一个节点），返回结果为复制后复杂链表的head。
    （注意，输出结果中请不要返回参数中的节点引用，否则判题程序会直接返回空）

思路：
    自己想的也是递归调用， 两条线路的递归，一条next, 一条random, 结果超过内存栈深度，最后看了讨论区，发现random那一条没必要因为可能会形成环。

'''
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution:

    '''
    time：20ms
    memory: 5728k
    '''

    def copy(self, pHead, node):
        if not pHead:
            return
        if pHead.next:
            node_next = RandomListNode(pHead.next.label)
            node.next = node_next
        node.random = pHead.random
        self.copy(pHead.next, node.next)

    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        if not pHead:
            return
        ans = RandomListNode(pHead.label)
        self.copy(pHead, ans)
        return ans
