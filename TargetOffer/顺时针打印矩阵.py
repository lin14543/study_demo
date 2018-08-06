# -*- coding:utf-8 -*-

'''

输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，例如，如果输入如下4 X 4矩阵： 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 则依次打印出数字1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.
找到边界， 然后一层一层地拨开它的心。。。。
'''

class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        if not len(matrix) or not len(matrix[0]):
            return
        row = len(matrix)
        col = len(matrix[0])
        x0, y0, x1, y1 = 0, 0, row, col
        ans = []
        while True:
            if x0 >= x1 or y0 >= y1:
                break
            for i in range(y0, y1):
                ans.append(matrix[x0][i])
            for i in range(x0 + 1, x1):
                ans.append(matrix[i][y1 - 1])
            if x1 - 1 != x0:  # 单行
                for i in range(y1 - 2, y0, -1):
                    ans.append(matrix[x1 - 1][i])
            if y1 - 1 != y0:  # 单列
                for i in range(x1 - 1, x0, -1):
                    ans.append(matrix[i][y0])
            x0 += 1
            y0 += 1
            x1 -= 1
            y1 -= 1
        return ans





