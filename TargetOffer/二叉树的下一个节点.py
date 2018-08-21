# -*- coding:utf-8 -*-

'''
题目描述：
    给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。
思路：
    题目看了好久才理解， 给出的这个节点不一定是根节点，只是一个树中的某一个节点
    所以分两种情况：
    如果该节点有右子节点，则中序遍历的下一个节点为以其右节点为根节点的树的最左节点
    如果该节点没有右子节点，则中序遍历的下一个节点为其含左子节点的父节点
'''

# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
class Solution:

    '''
    time: 38ms
    memory: 5724k
    '''

    def GetNext(self, pNode):
        # write code here
        if not pNode:
            return
        if pNode.right:
            flag = pNode.right
            while flag.left:
                flag = flag.left
            return flag
        else:
            while pNode.next:
                p = pNode.next
                left = p.left
                if left == pNode:
                    return p
                pNode = p
        return