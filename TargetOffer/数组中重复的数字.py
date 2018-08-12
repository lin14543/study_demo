# -*- coding:utf-8 -*-

'''
题目描述：
    在一个长度为n的数组里的所有数字都在0到n-1的范围内。 数组中某些数字是重复的，但不知道有几个数字是重复的。也不知道每个数字重复几次。
    请找出数组中任意一个重复的数字。 例如，如果输入长度为7的数组{2,3,1,0,2,5,3}，那么对应的输出是第一个重复的数字2。

思路：
    法一：用一个字典做标记。。。，
    法二：可以利用现有数组设置标志，当一个数字被访问过后，可以设置对应位上的数 + n，之后再遇到相同的数时，会发现对应位上的数已经大于等于n了，那么直接返回这个数即可。

'''

class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    '''
    time: 23ms
    memory: 5860k
    '''
    def duplicate(self, numbers, duplication):
        # write code here
        flag = {}
        for number in numbers:
            if flag.get(number):
                duplication[0] = number
                return True
            flag[number] = 1
        return False

class Solution2:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    '''
    time: 26ms
    memory: 5732k
    '''
    def duplicate(self, numbers, duplication):
        # write code here
        l = len(numbers)
        for i in range(l):
            index = numbers[i]
            if index >= l:
                index -= l
            if numbers[index] >= l:
                duplication[0] = index
                return True
            numbers[index] = numbers[index] + l
        return False