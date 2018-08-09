# -*- coding:utf-8 -*-

'''
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。

以前在ACM特训的时候刷过这道题，深深地被当时别人的解题思路所折服。现在重刷，需要注意的是边界问题， 如果数字出现次数超过一半，那在加加减减之后肯定还是它，但是需要注意边如果最终的ans是最后一位且flag=1 且该元素不止一位，那就是没有超过一半的数字了。

'''
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        flag = 1
        ans = numbers[0]
        for i in numbers[1:]:
            if i == ans:
                flag += 1
            else:
                flag -= 1
                if flag <= 0:
                    flag = 1
                    ans = i
        if numbers[-1] == ans and flag == 1 and not len(numbers) == 1:
            return 0
        return ans


if __name__ == '__main__':
    so = Solution()
    print(so.MoreThanHalfNum_Solution([1,2,3,2,4,2,5,2,3]))