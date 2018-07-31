# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if not len(rotateArray):
            return 0
        low = 0
        high = len(rotateArray) - 1
        while low < high:
            mid = (low + high) // 2
            if rotateArray[mid] > rotateArray[high]:
                low = mid + 1
            elif rotateArray[mid] == rotateArray[high]:
                high = high -1
            # else:
            #     high = mid
        return rotateArray[low]

    ans = []
    for ok, x in results:
        if ok:
            ans.append(x['path'])
    return ans
