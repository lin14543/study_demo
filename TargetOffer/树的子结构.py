# -*- coding:utf-8 -*-

'''
输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）
'''

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:

    def isSubtree(self, pRoot1, pRoot2):
        if pRoot2 == None:
            return True
        if pRoot1 == None:
            return False
        return pRoot1.val == pRoot2.val and self.isSubtree(pRoot1.left, pRoot2.left) and self.isSubtree(pRoot1.right,
                                                                                                        pRoot2.right)

    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        # if not pRoot2 or not pRoot1:
        if pRoot1 == None or pRoot2 == None:
            return False
        return self.isSubtree(pRoot1, pRoot2) or self.HasSubtree(pRoot1.left, pRoot2) or self.HasSubtree(pRoot1.right,
                                                                                                         pRoot2)
