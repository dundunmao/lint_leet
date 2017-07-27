# -*- encoding: utf-8 -*-
# 1 is read off as "one 1" or 11.
# 11 is read off as "two 1s" or 21.
# 21 is read off as "one 2, then one 1" or 1211.
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        cur = [1]
        while n != 1:
            cur = self.count(cur)
            n -= 1
        ans = [str(ele) for ele in cur]
        return ''.join(ans)
    def count(self,s):

        hash = {}
        array = []
        count = 1
        for i in range(1,len(s)):
            if s[i] != s[i-1]:
                array.append(count)
                array.append(s[i-1])
                count = 1
            else:
                count += 1
        array.append(count)
        array.append(s[-1])
        # return ''.join(array)
        return array
if __name__ == '__main__':
    s = Solution()
    n = 1
    print s.countAndSay(n)