# -*- coding:utf-8 -*-

'''
题目描述:
    给定一个数组A[0,1,...,n-1],请构建一个数组B[0,1,...,n-1],其中B中的元素B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]。不能使用除法。
思路：(来自：牛客网，很巧妙的解法)
    B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]
    从左到右算 B[i]=A[0]*A[1]*...*A[i-1]
    从右到左算B[i]*=A[i+1]*...*A[n-1]

'''

class Solution:

    '''
    time: 27ms
    memory: 5732k
    '''

    def multiply(self, A):
        # write code here
        multi = 1
        B = [multi]
        for i in range(len(A) - 1):
            multi *= A[i]
            B.append(multi)
        ret = 1
        for i in range(len(A) - 1, 0, -1):
            ret *= A[i]
            B[i - 1] *= ret
        return B
