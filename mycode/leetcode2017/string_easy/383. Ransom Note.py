# -*- encoding: utf-8 -*-
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        用杂志上的字符拼凑一封勒索信，字不能用两次
        """
        hash = {}
        for s in magazine:
            if hash.has_key(s):
                hash[s] += 1
            else:
                hash[s] = 1
        for s in ransomNote:
            if s in hash:
                hash[s] -= 1
                if hash[s] == 0:
                    del hash[s]
            else:
                return False
        return True
if __name__ == "__main__":
    a = 'aa'
    b = 'ab'
    x = Solution()
    print x.canConstruct(a,b)