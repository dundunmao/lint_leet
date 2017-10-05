# -*- encoding: utf-8 -*-
# two pointer.基本就是
# hash记录t的char频次
# count记录set(t)的char个数
# 循环开始，j往后走，每次hash里面的value=0，count就减1.
#       一旦count为0了，说明找到一组就更新返回值和最短距离。
#       这时候i要在while里往前走，一直走到遇到t里面的char，也就是count不为0时

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if len(s) < len(t):
            return ''
        res = ''
        count = len(set(t))   #count记录的是set(t)
        hash = {}
        distant = float('inf')
        for ele in t:        #建 hash，里面含频次
            hash[ele] = hash.setdefault(ele, 0) + 1
        i = 0
        j = -1
        while i < len(s) and j < len(s):
            while count == 0:   #当count为0时，处理更不更新distance和res，还要把i往前走，知道count不为0，就是i往外吐时吐出了t里的东西
                if distant > j - i + 1:
                    distant = j - i + 1
                    res = s[i:j + 1]
                if s[i] in hash:
                    hash[s[i]] += 1
                    if hash[s[i]] > 0:
                        count += 1
                i += 1
            j += 1              #每一轮j都要往后走一步，然后检查需不需要更新hash和count。
            if j < len(s) and s[j] in hash:
                hash[s[j]] -= 1
                if hash[s[j]] == 0:
                    count -= 1
        return res
if __name__ == "__main__":
    # a = [-3, -1, 4, 1, 5]
    # k = 2
    s = "bba"
    t = "ab"
    x = Solution()
    print x.minWindow(s,t)