# -*- coding:utf-8 -*-

'''
题目描述：
    从上到下按层打印二叉树，同一层结点从左至右输出。每一层输出一行。
解题思路：
    最早自己想的是一层while循环，用广度优先搜索遍历， 每层用None隔断开，但一直爆内存。。。。。
    看了评论区才发现有更好的方法，当队列里面有数据的时候，数据个数可不就是你要遍历的这层的个数嘛。。。一下就给过了。。。。
'''

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表[[1,2],[4,5]]
    '''
    time: 24ms
    memory: 5712k
    '''
    def Print(self, pRoot):
        # write code here
        if not pRoot:
            return []
        ans = []
        que = []
        que.append(pRoot)
        l = len(que)
        while l: # 当前层的结点个数
            flag = []
            for i in range(l):
                item = que.pop(0)
                flag.append(item.val)
                if item.left:
                    que.append(item.left)
                if item.right:
                    que.append(item.right)
            ans.append(flag)
            l = len(que)# 下一层的结点个数
        return ans