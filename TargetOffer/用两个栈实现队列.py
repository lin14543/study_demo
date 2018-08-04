# -*- coding:utf-8 -*-

'''
用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。
'''


"""
思路：
自己最开始的思路是入队时，直接入栈A即可，出队时。。先从栈A中倒出数据到栈B,然后再把栈B的栈顶元素弹出，再把数据倒回栈A,仔细一想，肯定有更优的解法，一搜如下：
入队时，将元素压入栈a
出队时，判断栈B中是否有元素，如果有直接弹出并返回，如果没有就把栈a中的元素倒入栈B,最后一个可不倒直接弹出返回即可。

"""

class Solution:
    def __init__(self):
        self.s_a = []
        self.s_b = []

    def push(self, node):
        self.s_a.append(node)

    def pop(self):
        if not len(self.s_b):
            for i in range(len(self.s_a) - 1):
                self.s_b.append(self.s_a.pop())
            return self.s_a.pop()
        else:
            return self.s_b.pop()