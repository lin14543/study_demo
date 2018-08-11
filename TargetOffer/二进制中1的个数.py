# -*- coding:utf-8 -*-
'''
输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。

思路好文：https://www.cnblogs.com/cotyb/archive/2016/02/11/5186461.html

'''
class Solution:
    def NumberOf1(self, n):
        # write code here
        ans = 0
        if n < 0:
            n = n & 0xffffffff # 消除负数的影响
        while n!=0:
            n = n & (n-1)
            ans += 1
        return ans

    def Numberof12(self, n):
        return bin(n).count('1') if n>=0 else bin(2 ** 32 + n).count("1") # 避免自己造轮子