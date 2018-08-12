# -*- coding:utf-8 -*-

'''
一个整型数组里除了两个数字之外，其他的数字都出现了偶数次。请写程序找出这两个只出现一次的数字。

思路：
法一：遍历一下数组，求出每个元素出现的次数，再遍历一遍，判断次数是否为1
法二：使用异或，相同数字异或两次结果为0，任何数对零异或，结果为原数。所以对数组中的所有数异或的结果就是只出现一次的两个数异或的结果，
     求出异或结果为1的最低位index,再以最低位为1的是否是index为判断依据对原数组分组，
     则这两组分别包含两个数中的一个，再异或得到两个数即可。
法三：pythonic. 利用collections中的Counter
'''

class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    '''
    time: 20ms
    memory: 5736k
    '''
    def FindNumsAppearOnce(self, array):
        # write code here
        ans_d = dict()
        for i in array:
            if i in ans_d:
                ans_d[i] += 1
            else:
                ans_d[i] = 1
        ans = []
        for k, v in ans_d.items():
            if v == 1:
                ans.append(k)
        return ans


class Solution2:
    # 返回[a,b] 其中ab是出现一次的两个数字

    '''
    time:21ms
    memory:5860k
    '''

    def FindNumsAppearOnce(self, array):
        # write code here
        temp = 0
        for i in array:
            temp ^= i
        idx = 0
        while temp & 1 == 0:
            idx += 1
            temp >>= 1
        ans = [0, 0]
        for i in array:
            if self.isBit(i, idx):
                ans[0] ^= i
            else:
                ans[1] ^= i
        return ans

    def isBit(self, num ,index):
        id = 0
        while num & 1 == 0:
            num >>= 1
            id += 1
        if id == index:
            return True
        return False


from collections import Counter
class Solution3:
    # 返回[a,b] 其中ab是出现一次的两个数字

    '''
    time: 24ms
    memory: 5728k
    '''
    def FindNumsAppearOnce(self, array):
        # write code here
        return [c[0] for c in Counter(array).most_common()[-2:]]
