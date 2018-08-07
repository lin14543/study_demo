# -*- coding:utf-8 -*-

'''
从上往下打印出二叉树的每个节点，同层节点从左至右打印。

思路： 最简单的bfs了。。。。。
'''

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]

    def PrintFromTopToBottom(self, root):
        # write code here
        que = [root]
        ans = []
        while len(que):
            top = que[0]
            que.pop(0)
            if not top:
                break
            if top.left:
                que.append(top.left)
            if top.right:
                que.append(top.right)
            ans.append(top.val)
        return ans
