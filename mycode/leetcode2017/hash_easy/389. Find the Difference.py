class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        hash = {}
        for str in s:
            if str not in hash:
                hash[str] = 1
            else:
                hash[str] += 1
        for str in t:
            if str not in hash or hash[str] == 0:
                return str
            else:
                hash[str] -= 1
