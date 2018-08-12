# -*- coding:utf-8 -*-

import re
class Solution:
    # s, pattern都是字符串
    '''
    time: 22ms
    memory: 5728k
    '''
    def match(self, s, pattern):
        # write code here
        return True if re.match("^" + pattern + '$', s) else False

class Solution1:
    # s, pattern都是字符串

    '''
    time: 22ms
    memory: 5728k
    '''

    def match(self, s, pattern):
        # write code here
        if s == '' and pattern == '':
            return True
        if s != '' and pattern == '':
            return False
        if len(pattern) <= 1 and pattern[1] != '*':
            if s[0] == pattern[0] or (s != '' and pattern[0] == '.'):
                return selfl.match(s[1:], pattern[1:])
            else:
                return False
        else:
            if s[0] == pattern[0] or (s != '' and pattern[0] == '.'):
                return self.match(s, pattern[2:]) or self.match(s[1:], pattern)
            else:
                return self.match(s, pattern[2:])

if __name__ == '__main__':
    so = Solution1()
    print(so.match('', '.*'))
