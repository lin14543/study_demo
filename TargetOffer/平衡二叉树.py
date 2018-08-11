# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

'''
输入一棵二叉树，判断该二叉树是否是平衡二叉树。

思路：所谓平衡二叉树，只要满足左右子树高度差不超过1即可，
一般思路：遍历每个结点，借助一个获取深度的递归函数，根据该结点的左右子树高度差判断是否平衡，然后递归地对左右子树进行判断。如Solution中的解法
这个做法在判断上层结点的时候，会多次重复遍历下层结点，增加了不必要的开销。如果改为从下往上遍历，如果子树是平衡二叉数，则返回子树的高度， 如果发现子树不是平衡二叉树，则直接停止遍历。
这种剪枝的做法至多只对每个结点访问一次。如Solution2.

'''
class Solution:
    def IsBalanced_Solution(self, pRoot):
        if not pRoot:
            return True
        return abs(self.getDepth(pRoot.left) - self.getDepth(pRoot.right)) <= 1 and self.IsBalanced_Solution(pRoot.left) and self.IsBalanced_Solution(pRoot.right)

    def getDepth(self, pRoot):
        if not pRoot:
            return 0
        return max(self.getDepth(pRoot.left), self.getDepth(pRoot.right)) + 1

class Solution2:

    def IsBalanced_Solution(self, pRoot):
        return self.getDepth(pRoot) != -1

    def getDepth(self, pRoot):
        if not pRoot:
            return 0
        left = self.getDepth(pRoot.left)
        if left == -1:
            return -1
        right = self.getDepth(pRoot.right)
        if right == -1:
            return -1
        return -1 if abs(left-right) > 1 else 1 + max(left, right)