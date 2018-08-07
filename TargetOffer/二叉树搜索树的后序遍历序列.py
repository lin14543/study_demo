# -*- coding:utf-8 -*-

'''
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。

思路：

//左子树一定比右子树小，因此去掉根后，数字分为left，right两部分，right部分的
//最后一个数字是右子树的根他也比左子树所有值大，因此我们可以每次只看右子树是否符合条件
//即可，即使到达了左子树左子树也可以看出由左右子树组成的树还想右子树那样处理
'''

class Solution:
    def VerifySquenceOfBST(self, sequence):
        l = len(sequence)
        if not l:
            return False
        l -= 1
        while l:
            i = 0
            while sequence[i] < sequence[l]:
                i += 1
            while sequence[i] > sequence[l]:
                i += 1
            if i < l:
                return False
            l -= 1
        return True