# -*- coding:utf-8 -*-

'''
题目描述
输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。例如输入数组{3，32，321}，则打印出这三个数字能排成的最小数字为321323。

思路：对该数组里的元素进行排序，按照前面数字的大小，func函数是精华
'''


def func(a, b):
    s1 = str(a) + str(b)
    s2 = str(b) + str(a)
    if s1 > s2:
        return -1
    if s2 > s1:
        return 1
    return 0

class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        print(numbers)
        list = sorted(numbers, func, reverse=True)
        print(list)
        print(numbers)
        ans = ''
        for i in list:
            ans += str(i)
        return ans

if __name__ == '__main__':
    so = Solution()
    print(so.PrintMinNumber([32, 3, 321]))