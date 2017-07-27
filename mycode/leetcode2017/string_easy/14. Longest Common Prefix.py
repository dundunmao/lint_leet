# -*- encoding: utf-8 -*-
# 有一个array of string，找到所有string的longest common prefix string
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ''
        if len(strs) == 1:
            return strs[0]
        le = float('inf')
        for s in strs:
            le = min(le,len(s))
        i = 0
        pre = []
        flag = True
        while i< le:
            ele=strs[0][i]
            for j in range(1,len(strs)):
                if strs[j][i] != ele:
                    flag = False
                    break
            if flag == False:
                break
            pre.append(ele)
            i += 1
        return ''.join(pre)

if __name__ == "__main__":
    a = ["aa","a"]
    x = Solution()
    print x.longestCommonPrefix(a)