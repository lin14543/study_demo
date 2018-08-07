# -*- coding:utf-8 -*-

'''
定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素的min函数（时间复杂度应为O（1））。

思路：定义一个辅助栈，入栈的时候，如果辅助栈为空或入栈元素小于等于辅助栈栈顶元素，则辅助栈与主栈同时添加该元素。
出栈时，如果主栈出栈元素等于辅助栈栈顶元素，则辅助栈与主栈同时出栈。
返回最小元素时，只需要返回辅助栈的栈顶元素即可。
'''

class Solution:
    def __init__(self):
        self.st1 = []
        self.st2 = []

    def push(self, node):
        # write code here
        self.st1.append(node)
        if not len(self.st2) or node <= self.st2[-1]:
            self.st2.append(node)

    def pop(self):
        # write code here
        if self.st1[-1] == self.st2[-1]:
            self.st2.pop()
        return self.st1.pop()

    def top(self):
        # write code here
        return self.st1[-1]

    def min(self):
        # write code here
        return self.st2[-1]
